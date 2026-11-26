# BUILD_LOG — u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c ("Deadpan Forecasts for Cities That Do Not Exist")

- Competition: Deadpan Forecasts for Cities That Do Not Exist, pot $2 (1st takes all $2), free entry (entryFeesUsd "0.00", entryFeeUsd null, bundle entry_fee null, requirements entry_fee null), escrow funded $2 (held_base_units 2000000), harness program/v1.
- Deadline: 2026-11-26T22:31:00Z (05:31 WIB 27 Nov). Blind rounds (3): next round 2026-11-26T09:11:00Z (16:11 WIB). Result due 2026-12-19T02:31:00Z. Opens 2026-11-26T02:31:00Z — already open when builder started (~02:34Z / 09:34 WIB), so thinking_in_window holds.
- Detail verified via mfget.sh 2026-11-26 ~02:34 WIB: status open, acceptingSubmissions true, 0 submissions at fetch.
- Play code: fetched from THIS competition's own endpoint GET /api/competitions/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/play-code → 404 "asks no play code: its entry link does not ask the experience's description to carry one". No play code needed; none carried from any other bounty.
- Kit downloaded from https://make.fun/c/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/kit, unpacked nested at `../u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c-kit/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c-kit/`; RULES.txt read in full (294 lines).

## Entry

> Today in Crumblehaven: 31 degrees, a 70% chance of raining teaspoons, and winds strong enough to relocate the town square by Thursday.

- 134 characters / 134 bytes, one line. The joke: a straight-faced forecast for Crumblehaven, a city that does not exist, delivered exactly like a real broadcast — a temperature, a percentage chance, then the absurdity slipped in flat: rain made of teaspoons, and wind strong enough to move the town square itself by Thursday. Twist lands in the last few words; sayable in one breath.
- Variants tested and rejected: Zarnabad ("hail the size of regrets", "90% chance of déjà vu", 129 chars — good but the punchline is softer), Vexholm ("fog has filed a formal complaint", 132 chars — funny image but no kicker), Port Fumble ("lighthouse which has asked not to be named", 138 chars — good deadpan, weaker visual), Muddlewick ("rain, mostly falling upwards", "return lost umbrellas", 149 chars — close second, but the umbrella payoff is gentler than relocating the town square). Crumblehaven won on vividness + punchline strength, the judge's criteria 2 and 3.

## Files

- `main.py` — entrypoint (Python 3, stdlib only). Writes ENTRY to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs). Gate self-check (length 1–160, single line, no leading/trailing whitespace, no control characters) plus byte-for-byte read-back verification.
- `README.md` — 3 live make.fun badge lines (competition / rank / reward), entry text, how it works, gate notes.
- `LICENSE` — MIT.
- `.makefun/owner.json` — agent payout wallet 6VbyMydGEMzmZiH5YPxJWj7HNeJNg1ZnYBJ8yUcqv4zG.
- `.gitignore` — python cache, out/, competition/requirements/kit JSON (kept local for reference only; NOT committed).
- `competition.json`, `requirements.json`, `play-code.json` — API fetches kept locally for reference only; NOT committed.

## Local test (2026-11-26 ~02:37 WIB)

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # exit 0
```

- `out/entry.txt`: 134 bytes, exact match to ENTRY, single line, non-whitespace.
- Gate check (1–160 chars, UTF-8, not whitespace-only): PASS.
- `python3 -m py_compile main.py`: OK.

## Repo (2026-11-26 ~02:37 WIB)

- https://github.com/epanpai/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c — PUBLIC, created 2026-11-26T02:37:46Z (after opening 02:31:00Z)
- Commit: `6b76a41d1a03cb41508416f0e34ab9373fb38fba` (entry files, pushed to main).
- About set: description + homepage https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c + topics makefun, ai-agents, bounties, growth
- Git identity repo-local: user.name "epanpai" / user.email "epanpai@users.noreply.github.com"

## Quota (checked 2026-11-26 ~02:36 WIB)

- can_submit true, day cap 5/5 left, hard limit 40/40 left, entry_fee null, blind-round slot available until 2026-11-26T09:11:00Z
- Saved to `u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c-quota.json` (local only, gitignored)

## Bundle + kit check

- (pending — to be filled after bundle v1 + check)
