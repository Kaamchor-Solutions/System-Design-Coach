# Worked example: personal reading list

> **Illustrative only:** fictional idea, not evidence about a real product or a security review.

**Status:** Proposed. **Evidence:** fictional brief; no existing code or deployment inspected.

**Need & success — Assumed:** One person wants to save links. Check: add a title and link, reopen the app in the same browser, and confirm it remains.

**Facts & assumptions — Observed:** None; this example is made up. **Assumed:** One person/device is enough at first. **Open question:** Must the list sync across devices now?

**Smallest useful solution — Proposed:** A page to add, list, and delete links, saved in browser-local storage (kept by this browser on this device). No account, server, or sync until evidence shows it is needed.

**Information flow — Proposed:** person → page → browser-local storage. No app-server transfer is proposed; network traffic and browser sync are untested, so privacy is not verified.

**Failure & trade-off:** Saved data could be cleared or lost. Titles and URLs may reveal sensitive interests; page code can read browser-local entries, and another person using the same profile might see them. Avoid sensitive notes; do not promise backup. Local storage avoids a server but has no built-in sync or recovery. Consider export or an account only after confirming need and privacy/access rules.

**Check & next step:** Add a harmless sample link, reopen the app, then delete it. Test the built page and inspect its data flows before making privacy claims. First decide whether one-device use is acceptable.

**Terms:** “Sync” means keeping copies on multiple devices. **MVP** means “minimum viable product,” the smallest first version that can test an idea; “first useful version” is clearer here. Browser-local storage is not a backup.
