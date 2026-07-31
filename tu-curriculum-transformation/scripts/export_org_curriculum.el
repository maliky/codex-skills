;;; export_org_curriculum.el --- Batch export TU curriculum Org files -*- lexical-binding: t; -*-

;; Usage:
;; emacs --batch --quick --load scripts/export_org_curriculum.el -- SOURCE.org

(defun tu-curriculum--prefer-user-org ()
  "Prefer a user-installed Org package when batch Emacs ships a stale Org."
  (let* ((elpa-dir (expand-file-name "~/.emacs.d/elpa"))
         (candidates
          (when (file-directory-p elpa-dir)
            (sort (directory-files elpa-dir t "^org-[0-9][-.0-9]*$") #'string>))))
    (when candidates
      (let* ((org-root (car candidates))
             (lisp-dir (expand-file-name "lisp" org-root)))
        (setq load-prefer-newer t)
        (setq load-path
              (cons (if (file-directory-p lisp-dir) lisp-dir org-root)
                    load-path))))))

(tu-curriculum--prefer-user-org)
(require 'org)
(require 'ox-latex)

(defun tu-curriculum--args-after-dash-dash ()
  "Return command-line arguments after --."
  (let ((args command-line-args-left))
    (if (and args (string= (car args) "--"))
        (cdr args)
      args)))

(defun tu-curriculum-export-main ()
  "Export the provided Org file to TeX and compile a PDF when possible."
  (let* ((args (tu-curriculum--args-after-dash-dash))
         (source (car args)))
    (unless source
      (message "Usage: emacs --batch --quick --load export_org_curriculum.el -- SOURCE.org")
      (kill-emacs 2))
    (unless (file-exists-p source)
      (message "Source not found: %s" source)
      (kill-emacs 1))
    (find-file source)
    (org-mode)
    (let ((tex-file (org-latex-export-to-latex)))
      (message "Exported TeX: %s" tex-file)
      (when (and tex-file (executable-find "lualatex"))
        (let ((default-directory
                (or (file-name-directory tex-file) default-directory))
              (tex-base (file-name-nondirectory tex-file)))
          (dotimes (pass 2)
            (let ((status
                   (call-process "lualatex" nil "*tu-curriculum-lualatex*" t
                                 "-interaction=nonstopmode" tex-base)))
              (unless (and (integerp status) (zerop status))
                (message "lualatex pass %d failed with status %s; log: %s"
                         (1+ pass) status "*tu-curriculum-lualatex*")
                (kill-emacs 1))))
          (message "Compile log buffer: *tu-curriculum-lualatex*"))))))

(tu-curriculum-export-main)

;;; export_org_curriculum.el ends here
