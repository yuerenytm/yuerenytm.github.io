(function () {
  var hero = document.querySelector("[data-hero]");
  if (!hero) return;

  var video = hero.querySelector("video");
  var motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");

  function still() {
    hero.classList.remove("is-playing");
    hero.classList.add("is-still");
    if (!video) return;
    video.pause();
    video.removeAttribute("src");
    var sources = video.querySelectorAll("source");
    for (var i = 0; i < sources.length; i += 1) {
      sources[i].removeAttribute("src");
      if (sources[i].parentNode) sources[i].parentNode.removeChild(sources[i]);
    }
    video.load();
  }

  function connectionSlow() {
    var connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (!connection) return false;
    if (connection.saveData) return true;
    return connection.effectiveType === "slow-2g" || connection.effectiveType === "2g";
  }

  var src = video && video.getAttribute("data-src");
  if (!video || !src || motionQuery.matches || connectionSlow()) {
    still();
    return;
  }

  function onMotionChange() {
    if (motionQuery.matches) still();
  }

  if (typeof motionQuery.addEventListener === "function") {
    motionQuery.addEventListener("change", onMotionChange);
  } else if (typeof motionQuery.addListener === "function") {
    motionQuery.addListener(onMotionChange);
  }

  video.muted = true;
  video.defaultMuted = true;
  video.playsInline = true;

  var source = document.createElement("source");
  source.src = src;
  source.type = video.getAttribute("data-type") || "video/mp4";
  source.addEventListener("error", still);
  video.addEventListener("error", still);
  video.addEventListener("playing", function () {
    if (!hero.classList.contains("is-still")) hero.classList.add("is-playing");
  });
  video.appendChild(source);
  video.load();

  var pending = video.play();
  if (pending && typeof pending.catch === "function") {
    pending.catch(function (error) {
      if (!error || error.name === "NotAllowedError") still();
    });
  }
})();
