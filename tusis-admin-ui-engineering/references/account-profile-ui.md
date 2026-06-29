# Account Profile UI

Use this reference when work touches the TUSIS self-service account/profile page or the deployment visibility of those UI changes.

## UI Pattern

- The account profile belongs inside the existing portal shell, not a new standalone page.
- High-signal files are usually:
  - `app/website/views/account.py`
  - `app/website/services/account_profile.py`
  - `app/website/templates/website/account_profile.html`
  - `app/website/static/css/staff-dashboard.css`
- Prefer dense grid or table-like presentation for read-only profile data.
- Keep all fields visible when the user chose "show all fields"; mark empty values with an `is_missing` style instead of hiding them.

## Typing And Fixtures

- `profile_kind()` distinguishes `Faculty` from `Staff` when a `Faculty` row exists for the staff profile.
- Keep the profile-kind type narrow, for example `Literal["Faculty", "Staff", "Student", "Donor", "Account"]`.
- Use an explicit saved-object guard such as `getattr(obj, "pk", None)` before relying on typed profile objects.
- In tests where a staff profile already exists, prefer `Faculty.objects.get_or_create(staff_profile=user.staff)` over direct `Faculty.objects.create(...)`.

## Validation

- On slow machines, keep checks focused; do not launch broad overlapping test runs.
- Useful focused checks include `ruff format`, `python -m py_compile`, `ruff check`, focused `mypy`, `python manage.py check`, and `git diff --check`.
- If a focused Django test fails first with PostgreSQL unreachable at `127.0.0.1:15432`, treat DB availability as the blocker.
- After CSS changes, run `python manage.py collectstatic --noinput` before judging served static behavior.

## VPS Visibility

- If the user says they are looking at `vps/dev`, verify that exact remote and branch.
- A bare repo can be current while the working checkout remains stale.
- Inspect `git remote -v` in the VPS checkout before pushing again.
- The known repair pattern was: add or fix the `vps` remote, `git fetch vps dev`, `git merge --ff-only vps/dev`, then `git fetch origin dev` so local status no longer reports misleading ahead/behind state.
