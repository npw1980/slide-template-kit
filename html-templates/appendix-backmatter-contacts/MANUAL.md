# appendix-backmatter-contacts — Back-Matter Contacts Roster

WHEN: The final content page of a report deck — "who to reach" — listing named engagement
contacts with role and e-mail. Derived from EY's "Ernst & Young LLP contacts" page (p25 of
ey__ey_generative_ai_in_wealth_and_asset_management_2024), read as a headshot-column roster; the
plain directory variant is EY European Banking Barometer 2015 p46. Use when the deck must name
owners for follow-up, not point at a generic inbox.

ANATOMY (1280×720 stage; all values in px):
1. Kicker — x56 y40 w1168 h14, 12px uppercase +10% tracking, name-blue.
2. Title — x56 y56 w1120, 30px display, max 2 lines, dark navy.
3. Rule — x56 y105 h2, bright blue, full content width (1168).
4. Group header "Authors" — x56 y172 w380 h16, 14px uppercase, gray-1.
5. Author entries — x56 y206, three stacked rows pitch 88 (avatar 52px at x56, id block at x122 w≈314).
6. Group header "Contributors" — x484 y172 w380.
7. Contributor entries — x484 y206, three stacked rows pitch 88.
8. Group header "Key contacts" — x884 y172 w320; column divided from Contributors by a 1px hairline at x856.
9. Key-contact entries — x884 y206, three rows pitch 76 (avatar 44px).
10. Source line — x56 y660 max-w 940, 10.5px gray-3, includes footnote marker a.
11. Page stamp + wordmark lockup — right 56 y660, "Page 25 | APPENDIX" + yellow-mark lockup.

SLOTS:
- kicker: ≤4 words. "Appendix — contacts" or "Back matter". Bad: a full sentence.
- title: ≤15 words / ≤2 lines. A purpose line ("Who to reach for…"), not just "Contacts" — the page still earns a claim-ish title.
- group-1 / group-2 / group-3: one word each (Authors / Contributors / Key contacts). A fourth group overflows the stage — max 3.
- name ×N: ≤20 chars. Real names. Font is semibold blue, so long names wrap to 2 lines inside 314px.
- role ×N: 2 lines max (explicit <br> per line), 11.5px. Two short lines beat one wrapping line.
- mail ×N: one line, 11px, break-all. Never a bare "contact us" — the point is a named owner.
- source-line: firm/roster provenance + as-of date. This page makes ownership claims, so it carries a footnote marker.
- page-stamp: "N | APPENDIX". Keep section label — the reader may re-enter mid-deck.

FILL:
1. Replace kicker, title text. Keep the rule (CSS handles it).
2. Each <article class="person">: swap .nm / .role / .mail. Duplicate or delete whole <article> blocks; row pitch is margin-based, no coordinate edits needed for 2–4 people per column.
3. Avatars: the SVG circles are placeholders (gray disc + white glyph). For real photos, replace the <svg class="avatar"> with <img> sized 52×52 (44 for key rows) and keep border-radius via a clip — but never fake a headshot with the glyph on a real deck; ship the photo or ship initials.
4. Recolor for a different house: --name (name text) and --accent (rule/kicker). --yellow marks the firm wordmark only.
5. Footnote marker <sup>a</sup> on the source line — add/remove to match real disclaimer text.

VERIFY:
- Title ≤15 words, ≤2 lines (rendering wraps at 1120px — count, don't trust).
- Source line present bottom-left with footnote marker; page stamp bottom-right.
- Exactly one hue (blue family) + gray ramp; yellow only inside the wordmark.
- Name blue on white clears 4.5:1 (that's why --name is a darkened shade, not the bright bar blue).
- No photo glyph left in place of a real headshot if photos exist.

DON'T:
- A wall of 15 contacts in one column — 3 columns × 3 rows is the ceiling; more people = a second appendix page.
- Titles that wrap to 3 lines — that's the signal to shorten the role, not shrink the font.
- Making names gray/black: names are the scannable layer, they take the accent family; roles recede.
- Duplicating one person in Authors and Key contacts without distinguishing why.
- Treating this as decoration: every named person must be someone who will actually answer the follow-up.

SOURCE: ey__ey_generative_ai_in_wealth_and_asset_management_2024, "Ernst & Young LLP contacts" p25
(sheet sw_sheets/ey__ey_generative_ai_in_wealth_and_asset_management_2024_s02.jpg, row 1 frame 5);
directory-roster variant ey__ey_european_banking_barometer_2015_2015 p46
(sheet .../ey__ey_european_banking_barometer_2015_2015_s04.jpg). Palette conventions from
reviews/ey__ey_generative_ai_in_wealth_and_asset_management_2024.md §Color system.
