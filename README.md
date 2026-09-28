# ACCESSION FILE AL-01

**Object:** Archive Lantern, a shared GenLayer label workshop for public history.

## Gallery premise

A curator freezes audience, interpretation principles, and ordered object facts. Distinct wallets draft one label each. The contract stores the light position, accepted labels, dim count, contributors, and terminal state.

## Label standard

Validators independently check factual fidelity, audience clarity, principles, and unsupported provenance or certainty. GenLayer matters because interpretation is qualitative while canonical public labels should not depend on one curator. `install` creates the exhibit; `draft_label` advances one plinth or one dim. All objects yield `EXHIBITION_OPEN`; three dims yield `DARK`.

## Interpreter route

The gallery reads `get_exhibit`, paged reviews, paged exhibits, and summary. Normalized IDs, duplicate rejection, unique interpreters, bounded inputs, and terminal guards run before consensus. State writes occur only after the agreed result.

## Installation commands

```text
genvm-lint lint contracts/contract.py
python -m pytest tests/test_surface.py -q
cd frontend
npm install
npm run typecheck
npm run build
```

The static Next.js frontend uses `genlayer-js`. Plinths, accession tabs, lantern masks, brass rails, label embossing, and gallery reveals form its visual system.

## Public installation

- StudioNet contract: `0xF02b12457EC0AEC3FBB84Dd03Eab6bdA2867969e`
- Deployment transaction: `0xe3a37df4c011afc813757d879d037c0420e3968dfe87a08d3c91cfed649a5493`
- Repository: https://github.com/wakbowaa/archive-lantern
- Gallery: https://archive-lantern.pages.dev/

## Conservation note

This workshop does not certify provenance, ownership, authenticity, restitution, or professional museum interpretation. The current StudioNet deployment finalized with `MAJORITY_AGREE` and leader execution `SUCCESS`.
