# Architecture Overview

- Aiken contracts implement on-chain invariants for lock/borrow/repay/liquidation.
- Off-chain CLI/agents provide oracle price feeds as reference inputs and construct transactions that include oracle data.
- Partial liquidation is computed off-chain and passed as a parameter to the liquidation redeemer.
- Evidence is produced as tx IDs and stored in reports/evidence/.
