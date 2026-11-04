# Portfolio Comparison At Startup Prices

Use when the user asks how the account changed if current holdings were valued at the bot's startup prices, with no further trades or closures. Report contributions per symbol. Keep this counterfactual valuation separate from closed-cycle PnL and actual liquidation proceeds.

## Baseline And Evidence

Identify the run start, a complete account snapshot near that time, and a complete current snapshot from the same account/environment. State any baseline time offset and gaps. Record startup prices for each instrument and the FX rates used to value collateral; state which prices are held fixed. Fetch current evidence through the appropriate account workflow without inferring holdings or balances from bot logs.

Use each snapshot's actual holdings, position quantities, entry bases and accrued amounts. Revalue them with the instrument's payout model and contract units at the same reference prices. Reconcile to account equity, rather than valuing leveraged contracts as if the whole position notional were owned cash. If only instrument prices are restored while collateral FX stays current, label that as a different comparison.

## Per-Symbol Attribution

- For each symbol, combine attributable net cash changes since baseline with the change in open-position valuation at the reference price. Include realised PnL, observed fees and settled funding once; add the change in accrued funding only if it is not already included in cash or the chosen valuation field.
- Reconcile deposits, withdrawals, transfers, currency conversions and unrelated adjustments separately. Show raw equity change and flow-adjusted change when relevant; do not label an external contribution as strategy profit.
- Shared collateral remains account-wide. Do not divide it arbitrarily between symbols or claim a symbol owns a separate portfolio. Label symbol rows as contributions to the total, with unattributed items or reconciliation residuals visible.
- Preserve missing fee, funding, position or conversion evidence as unknown. State any estimate and its effect on the result; avoid claiming an exact attribution from incomplete history.

Show reference/current snapshot times, reference prices, each symbol's cash and open-valuation changes, net contribution, and the reconciled account total. Hold further trading, funding accrual and closing fees outside the scenario unless explicitly modelled; include funding already accrued at the observation time without counting it twice.
