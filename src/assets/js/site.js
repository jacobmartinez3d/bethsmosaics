(() => {
  "use strict";

  const menu = document.querySelector(".menu-toggle");
  const navigation = document.querySelector(".site-nav");
  const mobile = window.matchMedia("(max-width: 760px)");

  if (menu && navigation) {
    let expanded = false;

    const setExpanded = (value, restoreFocus = false) => {
      expanded = value;
      menu.setAttribute("aria-expanded", String(expanded));
      navigation.hidden = mobile.matches && !expanded;
      if (restoreFocus) menu.focus();
    };

    menu.hidden = false;
    document.documentElement.classList.add("js");
    setExpanded(false);
    menu.addEventListener("click", () => setExpanded(!expanded));
    navigation.addEventListener("click", (event) => {
      if (event.target.closest("a") && mobile.matches) setExpanded(false);
    });
    mobile.addEventListener("change", () => {
      const focusInNavigation = navigation.contains(document.activeElement);
      setExpanded(false, mobile.matches && focusInNavigation);
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && mobile.matches && expanded && !document.querySelector("dialog[open]")) {
        event.preventDefault();
        setExpanded(false, true);
      }
    });
  }

  const dialog = document.querySelector("#artwork-lightbox");
  const gallery = Array.from(document.querySelectorAll(".artwork-grid .artwork-image-link"));
  if (!dialog || !gallery.length || typeof dialog.showModal !== "function") return;

  const fullImage = dialog.querySelector("img");
  const title = dialog.querySelector("#lightbox-title");
  const close = dialog.querySelector(".lightbox-close");
  let current = 0;
  let opener;

  const showPhoto = (index) => {
    current = (index + gallery.length) % gallery.length;
    const link = gallery[current];
    const thumbnail = link.querySelector("img");
    fullImage.src = link.getAttribute("href");
    fullImage.alt = thumbnail.alt;
    fullImage.width = Number(thumbnail.getAttribute("width"));
    fullImage.height = Number(thumbnail.getAttribute("height"));
    title.textContent = link.dataset.artworkTitle;
  };

  document.querySelectorAll(".artwork-image-link").forEach((link) => {
    link.setAttribute("aria-haspopup", "dialog");
    link.addEventListener("click", (event) => {
      if (event.defaultPrevented || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      opener = link;
      showPhoto(gallery.findIndex((photo) => photo.getAttribute("href") === link.getAttribute("href")));
      dialog.showModal();
      document.body.classList.add("lightbox-open");
      close.focus({ preventScroll: true });
    });
  });

  close.addEventListener("click", () => dialog.close());
  dialog.querySelector(".lightbox-previous").addEventListener("click", () => showPhoto(current - 1));
  dialog.querySelector(".lightbox-next").addEventListener("click", () => showPhoto(current + 1));
  dialog.addEventListener("keydown", (event) => {
    if (event.ctrlKey || event.metaKey || event.altKey) return;
    if (event.key === "Tab") {
      const controls = Array.from(dialog.querySelectorAll("button"));
      const first = controls[0];
      const last = controls[controls.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
    if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
      event.preventDefault();
      showPhoto(current + (event.key === "ArrowLeft" ? -1 : 1));
    }
  });

  const outside = (event) => {
    const bounds = dialog.getBoundingClientRect();
    return event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom;
  };
  let backdropPress = false;
  dialog.addEventListener("pointerdown", (event) => { backdropPress = outside(event); });
  dialog.addEventListener("click", (event) => {
    if (backdropPress && outside(event)) dialog.close();
    backdropPress = false;
  });
  dialog.addEventListener("close", () => {
    document.body.classList.remove("lightbox-open");
    opener?.focus({ preventScroll: true });
  });
})();
