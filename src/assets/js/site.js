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
      if (event.key === "Escape" && mobile.matches && expanded) {
        event.preventDefault();
        setExpanded(false, true);
      }
    });
  }
})();
