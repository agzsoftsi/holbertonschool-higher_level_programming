/* Task 9 -script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML’s tag DIV#hello
The translation of "hello" must be display in the HTML tag DIV#hello
You must use the jQuery API
Your script must work when it is imported from the HEAD tag
Use getJSON to call the API for https://fourtonfish.com/hellosalut/hello/
Supported browser languages:
ar, az, be, bg, bn, bs, cs, da, de, dz, el, en, en-gb, en-us, es, et, fa, fi, fil, fr, he, hi, hr, hu, hy, id, is, it, ja, ka, kk, km, ko, lb, lo, lt, lv, mk, mn, ms, my, ne, no, pl, pt, ro, ru, sk, sl, sq, sr, sv, sw, th, tk, uk, vi, zh
*/
$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (query) {
  $('#hello').text(query.hello);
});
