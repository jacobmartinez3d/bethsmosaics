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

  const images = document.querySelectorAll("img[data-enlarge]");
  if (!images.length || typeof HTMLDialogElement === "undefined" || !HTMLDialogElement.prototype.showModal) return;

  const dialog = document.createElement("dialog");
  dialog.className = "image-dialog";
  const closeButton = document.createElement("button");
  closeButton.type = "button";
  closeButton.className = "dialog-close";
  closeButton.textContent = "Close";
  const fullImage = document.createElement("img");
  fullImage.decoding = "async";
  dialog.append(closeButton, fullImage);
  document.body.append(dialog);

  let activeTrigger;
  closeButton.addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (event) => {
    const bounds = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom)) {
      dialog.close();
    }
  });
  dialog.addEventListener("close", () => {
    document.body.classList.remove("dialog-open");
    activeTrigger?.focus({ preventScroll: true });
  });

  images.forEach((image) => {
    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "enlarge-button";
    trigger.setAttribute("aria-haspopup", "dialog");
    const arrow = document.createElement("span");
    arrow.setAttribute("aria-hidden", "true");
    arrow.textContent = "↗";
    trigger.append("View full image ", arrow);
    image.after(trigger);
    trigger.addEventListener("click", () => {
      activeTrigger = trigger;
      fullImage.src = image.src;
      fullImage.alt = image.alt;
      fullImage.width = image.width;
      fullImage.height = image.height;
      dialog.setAttribute("aria-label", "Full image: " + document.querySelector("h1").textContent);
      document.body.classList.add("dialog-open");
      dialog.showModal();
    });
  });
})();
