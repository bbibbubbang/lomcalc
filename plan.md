1. **Rename "직접 입력 데미지 설정" and Modify Inputs:**
   - Change the header text from "직접 입력 데미지 설정" to "추가 데미지".
   - Keep `attackPct`, `defensePct`, `hpPct`, `advAttackPct`, `advDefensePct`, `advHpPct` in this section. Their values will now be additively applied to the calculation instead of being used to reverse-calculate the base stats.
2. **Add "마을 능력치" Section:**
   - Create a new collapsible section "마을 능력치".
   - Move `finalAttack`, `finalDefense`, `finalHP` inputs into this section.
   - Move all Platinum Maple Leaf inputs into this section.
   - Add new inputs: `townAttackPct`, `townDefensePct`, `townHpPct` in this section.
   - Update `calculate()` so `originalAttack`, `originalDefense`, `originalHP` are derived from the town final stats using the new `town...Pct` inputs and the Maple Leaf flat bonuses.
3. **Update "실제 능력치" UI:**
   - Change grid to `md:grid-cols-4`.
   - Add a new "기본 능력치" column on the far left. It will display the derived `originalAttack`, `originalDefense`, and `originalHP`.
   - Rename "기본 및 직업" column header to "추가 능력치".
4. **Implement Foldable State Persistence for Sections:**
   - Save the open/collapsed state of all sections ("장비 설정", "아티팩트 설정", "마을 능력치", "추가 데미지", "실제 능력치") in cookies/localStorage.
   - Set "장비 설정" and "아티팩트 설정" to be collapsed by default initially.
   - Restore the saved state upon page load in `loadSettings()`.
5. **Complete pre-commit steps:**
   - Run required pre-commit checks and verification to ensure proper testing, verifications, reviews and reflections are done.
6. **Submit changes:**
   - Once everything is verified, submit the code.
