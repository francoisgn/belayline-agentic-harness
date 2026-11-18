# A required UI or end-to-end verification step run by an agent

- **Asked in:** [#145](https://github.com/francoisgn/belayline-agentic-harness/issues/145) (LinkedIn comment on the
  launch post, 2026-11-18: an agent that tests the interface through a browser or emulator, to cut manual tests)
- **Decision:** declined as a core step on 2026-11-18; documented as an optional project step
- **Why:** it fails the toolbox test of [SCOPE.md](../SCOPE.md): many projects have no interface, and a required step
  would bring a browser or emulator into every project. The method already has the slot: an optional UI check whose
  result goes under "Verified" or "Watch points / not tested" (METHODOLOGY §2 ter.6), plugged in by the project
  ([ADOPTION](../docs/ADOPTION.md#plugging-a-step-before-or-after-the-loop)).
- **What would change the answer:** several consumer projects shipping UI regressions that passed both reviews and
  the optional step, where a shared harness building block would have caught them.
