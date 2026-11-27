<h2><a href="https://www.codechef.com/problems/NEWCC" target="_blank" rel="noopener noreferrer">NEWCC — Welcome to the CodeChef AI Tutor</a></h2>

| | |
|---|---|
| **Difficulty** | Difficulty:354 |
| **Language** | Python3​ |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [CodeChef NEWCC](https://www.codechef.com/problems/NEWCC) |

## Topics
_No tags available_

---

## Problem Statement

<div class="_problemStatementWrapper_bh3c4_33"><div class="_problemBodyContent_bh3c4_71"><h3 class="notranslate">All New CodeChef</h3><p><em>CodeChef has just finished <a href="https://discuss.codechef.com/t/migration-to-new-judging-system/109033" target="_blank">migrating</a> to a new judging system.</em></p>
<p>Chef would like to test the performance of the new judging system.</p>
<p>Chef has some code for an older task, which he knows ran in <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6833em;"></span><span class="mord mathnormal" style="margin-right: 0.07847em;">X</span></span></span></span></span> milliseconds on the old judging server.<br>
On resubmitting the code to the new judging server, it ran in <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>Y</mi></mrow><annotation encoding="application/x-tex">Y</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6833em;"></span><span class="mord mathnormal" style="margin-right: 0.22222em;">Y</span></span></span></span></span> milliseconds.</p>
<p>Which judging system is faster?</p>
<div class="notranslate">
<h3>Input Format</h3>
<ul>
<li>The only line of input will contain two space-separated integers <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6833em;"></span><span class="mord mathnormal" style="margin-right: 0.07847em;">X</span></span></span></span></span> and <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>Y</mi></mrow><annotation encoding="application/x-tex">Y</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6833em;"></span><span class="mord mathnormal" style="margin-right: 0.22222em;">Y</span></span></span></span></span> — the runtime on the old judging system, and the runtime on the new judging system.</li>
</ul>
</div><div class="notranslate">
<h3>Output Format</h3>
<p>Print:</p>
<ul>
<li><code>Old</code>, if the older judging system is faster</li>
<li><code>New</code>, if the new judging system is faster</li>
<li><code>Same</code>, if they're equally fast</li>
</ul>
<p>Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings <code>Old</code>, <code>OlD</code>, <code>old</code>, <code>oLD</code> will all be treated as equivalent.</p>
</div>
<h3 class="notranslate">Constraints</h3>
<div class="_html_code__block_bh3c4_219 notranslate">
<ul>
<li><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>≤</mo><mi>X</mi><mo separator="true">,</mo><mi>Y</mi><mo>≤</mo><mn>3000</mn></mrow><annotation encoding="application/x-tex">1 \leq X, Y \leq 3000</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.7804em; vertical-align: -0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.8778em; vertical-align: -0.1944em;"></span><span class="mord mathnormal" style="margin-right: 0.07847em;">X</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.1667em;"></span><span class="mord mathnormal" style="margin-right: 0.22222em;">Y</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">3000</span></span></span></span></span></li>
</ul>
</div>
<h3 class="notranslate">Sample 1:</h3>
<div class="_input_output__table_bh3c4_231 notranslate"><div class="_text_copy__container_bh3c4_235"><div class="_text_copy_bh3c4_235 _input_top__box_bh3c4_248"><span>Input</span><div aria-label="Copy to clipboard" class="undefined css-1eiukdk" style="pointer-events: all;"><span class="_icon__box_10bs7_2 _dark_10bs7_27 undefined"><i class="_copy__icon_10bs7_14"></i></span></div></div><div class="_text_copy_bh3c4_235 _ouput_top__box_bh3c4_251"><span>Output</span><div aria-label="Copy to clipboard" class="undefined css-1eiukdk" style="pointer-events: all;"><span class="_icon__box_10bs7_2 _dark_10bs7_27 undefined"><i class="_copy__icon_10bs7_14"></i></span></div></div></div><div class="_values__container_bh3c4_254"><div class="_values_bh3c4_254"><pre>255 230</pre></div><div class="_values_bh3c4_254"><pre>New</pre></div></div></div>
<h3 class="notranslate">Explanation:</h3>
<div class="notranslate">
<p>The code ran in <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>255</mn></mrow><annotation encoding="application/x-tex">255</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">255</span></span></span></span></span> ms on the old judging system, and <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>230</mn></mrow><annotation encoding="application/x-tex">230</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">230</span></span></span></span></span> ms on the new one.<br>
The new one is faster.</p>
</div>
<h3 class="notranslate">Sample 2:</h3>
<div class="_input_output__table_bh3c4_231 notranslate"><div class="_text_copy__container_bh3c4_235"><div class="_text_copy_bh3c4_235 _input_top__box_bh3c4_248"><span>Input</span><div aria-label="Copy to clipboard" class="undefined css-1eiukdk" style="pointer-events: all;"><span class="_icon__box_10bs7_2 _dark_10bs7_27 undefined"><i class="_copy__icon_10bs7_14"></i></span></div></div><div class="_text_copy_bh3c4_235 _ouput_top__box_bh3c4_251"><span>Output</span><div aria-label="Copy to clipboard" class="undefined css-1eiukdk" style="pointer-events: all;"><span class="_icon__box_10bs7_2 _dark_10bs7_27 undefined"><i class="_copy__icon_10bs7_14"></i></span></div></div></div><div class="_values__container_bh3c4_254"><div class="_values_bh3c4_254"><pre>1045 1309</pre></div><div class="_values_bh3c4_254"><pre>Old</pre></div></div></div>
<h3 class="notranslate">Explanation:</h3>
<div class="notranslate">
<p>The code ran in <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1045</mn></mrow><annotation encoding="application/x-tex">1045</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">1045</span></span></span></span></span> ms on the old judging system, and <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1309</mn></mrow><annotation encoding="application/x-tex">1309</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">1309</span></span></span></span></span> ms on the new one.<br>
The old one is faster.</p>
</div><div></div></div></div>