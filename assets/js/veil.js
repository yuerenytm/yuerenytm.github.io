(function () {
  var KEY = "dz-veil";
  var input = document.querySelector("[data-veil]");
  if (!input) return;

  var root = document.documentElement;
  var stored = null;
  try {
    stored = window.localStorage.getItem(KEY);
  } catch (e) {}

  var value = stored === null ? 0.6 : parseFloat(stored);
  if (isNaN(value)) value = 0.6;
  value = Math.min(1, Math.max(0, value));

  function apply(v) {
    root.style.setProperty("--veil", v.toFixed(2));
  }

  input.value = value;
  apply(value);

  input.addEventListener("input", function () {
    apply(parseFloat(input.value));
  });

  input.addEventListener("change", function () {
    try {
      window.localStorage.setItem(KEY, input.value);
    } catch (e) {}
  });
})();
