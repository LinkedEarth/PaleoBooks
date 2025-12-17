var buttons = document.querySelectorAll('.modal-btn')
var backdrop = document.querySelector('.modal-backdrop')
var modals = document.querySelectorAll('.modal')

function openModal(i) {
  backdrop.style.display = 'block'
  modals[i].style.display = 'block'
}

function closeModal(i) {
  backdrop.style.display = 'none'
  modals[i].style.display = 'none'
}

for (var i = 0; i < buttons.length; i++) {
  (function (j) {
    buttons[j].addEventListener('click', function () {
      openModal(j);
    });
    if (backdrop) {
      backdrop.addEventListener('click', function () {
        closeModal(j);
      });
    }
  })(i);
}

// =========================
// FILTERING HELPERS
// =========================

// Read the rel attributes of all checked checkboxes in a group.
// function getClassOfCheckedCheckboxes(checkboxes) {
//   var classes = [];
//
//   if (checkboxes && checkboxes.length > 0) {
//     for (var i = 0; i < checkboxes.length; i++) {
//       var cb = checkboxes[i];
//       if (cb.checked) {
//         classes.push(cb.getAttribute("rel"));
//       }
//     }
//   }
//
//   return classes;
// }

function getClassOfCheckedCheckboxes(checkboxes) {
  var classes = [];
  if (!checkboxes || checkboxes.length === 0) return classes;

  for (var i = 0; i < checkboxes.length; i++) {
    var cb = checkboxes[i];
    if (cb.checked) {
      classes.push(cb.getAttribute("rel"));
    }
  }
  return classes;
}


// Robust class matcher that tolerates leading digits being stripped.
function hasTagClass(el, cls, group) {
  if (!cls) return false;

  var raw = cls.toString();

  // Original code lowercased formats
  if (group === "formats") {
    raw = raw.toLowerCase();
  }

  // 1) Exact
  if (el.classList.contains(raw)) return true;

  // 2) Lowercase
  var lower = raw.toLowerCase();
  if (el.classList.contains(lower)) return true;

  // 3) Docutils-style: strip leading non-letters, e.g. "2k-foo" -> "k-foo"
  var normalized = lower.replace(/^[^a-zA-Z]+/, "");
  if (normalized && el.classList.contains(normalized)) return true;

  return false;
}

// Build the filters object and apply filtering.
function change() {
  console.log("change() triggered");

  var affiliationCbs = document.querySelectorAll(".affiliation input[type='checkbox']");
  var bookCbs        = document.querySelectorAll(".book input[type='checkbox']");
  var langCbs        = document.querySelectorAll(".language input[type='checkbox']");
  var domainsCbs     = document.querySelectorAll(".domains input[type='checkbox']");
  var formatsCbs     = document.querySelectorAll(".formats input[type='checkbox']");
  var packagesCbs    = document.querySelectorAll(".packages input[type='checkbox']");
  var publishedCbs   = document.querySelectorAll(".published input[type='checkbox']");

  var filters = {
    affiliation: getClassOfCheckedCheckboxes(affiliationCbs),
    domains:     getClassOfCheckedCheckboxes(domainsCbs),
    formats:     getClassOfCheckedCheckboxes(formatsCbs),
    packages:    getClassOfCheckedCheckboxes(packagesCbs),
    book:        getClassOfCheckedCheckboxes(bookCbs),
    language:    getClassOfCheckedCheckboxes(langCbs),
    published:   getClassOfCheckedCheckboxes(publishedCbs)
  };

  console.log("Filters applied:", filters);
  filterResults(filters);
}

function filterResults(filters) {
  var cards = document.querySelectorAll(".sd-tagged-card");
  console.log("filterResults(): cards found =", cards.length);
  if (!cards || cards.length === 0) return;

  // Helper: does this card have a class matching the filter value?
  function hasTagClass(el, cls, group) {
    if (!cls) return false;

    var raw = cls.toString();

    // 1) Exact match, as-is:
    if (el.classList.contains(raw)) return true;

    // 2) Lowercase:
    var lower = raw.toLowerCase();
    if (el.classList.contains(lower)) return true;

    // 3) Strip leading non-letters to cope with docutils/sphinx normalizing
    //    "2k-proxy-composite" -> "k-proxy-composite"
    var normalized = lower.replace(/^[^a-zA-Z]+/, "");
    if (normalized && el.classList.contains(normalized)) return true;

    // 4) If spaces ever appear in tags in future, normalize them as hyphens too
    var hyphenated = normalized.replace(/\s+/g, "-");
    if (hyphenated && el.classList.contains(hyphenated)) return true;

    return false;
  }

  cards.forEach(function (el, i) {
    var hide = false;

    function fails(group) {
      var list = filters[group];
      // No filters selected for this group -> pass
      if (!list || list.length === 0) return false;

      // Need to match AT LEAST ONE tag in this group
      for (var j = 0; j < list.length; j++) {
        var cls = list[j];
        if (hasTagClass(el, cls, group)) {
          return false; // passes this group
        }
      }
      return true; // failed this group
    }

    // Combine all groups (AND across groups, OR within group)
    if (
      fails("affiliation") ||
      fails("book") ||
      fails("published") ||
      fails("language") ||
      fails("domains") ||
      fails("formats") ||
      fails("packages")
    ) {
      hide = true;
    }

    if (hide) {
      el.classList.remove("d-flex");
      el.classList.add("d-none");
    } else {
      el.classList.remove("d-none");
      el.classList.add("d-flex");
    }
    // var wrapper = el.closest(".sd-col") || el;
    //
    // if (hide) {
    //   wrapper.classList.add("d-none");
    // } else {
    //   wrapper.classList.remove("d-none");
    // }
  });
}

//
// // Core filtering logic: AND across groups, OR within a group.
// function filterResults(filters) {
//   var cards = document.querySelectorAll(".sd-tagged-card");
//   console.log("filterResults(): cards found =", cards.length);
//   if (!cards || cards.length === 0) return;
//
//   var groups = [
//     "affiliation",
//     "book",
//     "published",
//     "language",
//     "domains",
//     "formats",
//     "packages"
//   ];
//
//   for (var i = 0; i < cards.length; i++) {
//     var el = cards[i];
//     var hide = false;
//
//     // Decide visibility for this card
//     for (var g = 0; g < groups.length; g++) {
//       var group = groups[g];
//       var list = filters[group];
//
//       // No filters selected in this group => no constraint from this group
//       if (!list || list.length === 0) continue;
//
//       var matchesGroup = false;
//       for (var j = 0; j < list.length; j++) {
//         var cls = list[j];
//         if (hasTagClass(el, cls, group)) {
//           matchesGroup = true;
//           break;
//         }
//       }
//
//       // If it fails any active group, hide it
//       if (!matchesGroup) {
//         hide = true;
//         break;
//       }
//     }
//
//     // Hide/show the outer column wrapper if present, otherwise the card
//     var wrapper = el.closest(".sd-col") || el;
//
//     if (hide) {
//       wrapper.classList.add("d-none");
//     } else {
//       wrapper.classList.remove("d-none");
//     }
//   }
// }

function clearCbs() {
  var selectors = [
    ".book",
    ".affiliation",
    ".domains",
    ".formats",
    ".packages",
    ".language",
    ".published"
  ];

  selectors.forEach(function (selector) {
    var cbs = document.querySelectorAll(selector + " input[type='checkbox']");
    for (var i = 0; i < cbs.length; i++) {
      cbs[i].checked = false;
    }
  });

  change();
}

// Wire up checkbox change events after DOM is ready.
document.addEventListener("DOMContentLoaded", function () {
  console.log("Filter init: wiring checkbox listeners");

  var selector = [
    ".affiliation input[type='checkbox']",
    ".book input[type='checkbox']",
    ".language input[type='checkbox']",
    ".domains input[type='checkbox']",
    ".formats input[type='checkbox']",
    ".packages input[type='checkbox']",
    ".published input[type='checkbox']"
  ].join(",");

  var allCbs = document.querySelectorAll(selector);
  for (var i = 0; i < allCbs.length; i++) {
    allCbs[i].addEventListener("change", change);
  }

  // Initial state: show all cards
  change();
});


//
// function change() {
//     console.log("change() triggered");
//
//   var affiliationCbs = document.querySelectorAll(".affiliation input[type='checkbox']");
//   var bookCbs        = document.querySelectorAll(".book input[type='checkbox']");
//   var langCbs        = document.querySelectorAll(".language input[type='checkbox']");
//   var domainsCbs     = document.querySelectorAll(".domains input[type='checkbox']");
//   var formatsCbs     = document.querySelectorAll(".formats input[type='checkbox']");
//   var packagesCbs    = document.querySelectorAll(".packages input[type='checkbox']");
//   var publishedCbs   = document.querySelectorAll(".published input[type='checkbox']");
//
//   var filters = {
//     affiliation: getClassOfCheckedCheckboxes(affiliationCbs),
//     domains:     getClassOfCheckedCheckboxes(domainsCbs),
//     formats:     getClassOfCheckedCheckboxes(formatsCbs),
//     packages:    getClassOfCheckedCheckboxes(packagesCbs),
//     book:        getClassOfCheckedCheckboxes(bookCbs),
//     language:    getClassOfCheckedCheckboxes(langCbs),
//     published:   getClassOfCheckedCheckboxes(publishedCbs),
//      runnable: []  // <-- add this line
//   };
//   console.log("Filters applied:", filters);
//   filterResults(filters);
// }
//
//
// function getClassOfCheckedCheckboxes(checkboxes) {
//   var classes = [];
//
//   if (checkboxes && checkboxes.length > 0) {
//     for (var i = 0; i < checkboxes.length; i++) {
//       var cb = checkboxes[i];
//       if (cb.checked) {
//         classes.push(cb.getAttribute("rel"));
//       }
//     }
//   }
//
//   return classes;
// }
//
//
// function hasTagClass(el, cls, group) {
//   if (!cls) return false;
//
//   // Start from the raw filter value
//   var raw = cls.toString();
//
//   // For formats, original code used lowercase
//   if (group === "formats") {
//     raw = raw.toLowerCase();
//   }
//
//   // 1) Exact match
//   if (el.classList.contains(raw)) return true;
//
//   // 2) Lowercase match (just in case)
//   var lower = raw.toLowerCase();
//   if (el.classList.contains(lower)) return true;
//
//   // 3) Docutils-style: strip leading non-letters (e.g. "2k-foo" -> "k-foo")
//   var normalized = lower.replace(/^[^a-zA-Z]+/, "");
//   if (normalized && el.classList.contains(normalized)) return true;
//
//   return false;
// }
//
// var PASS_INDEX = 7;  // <-- replace with whatever that findIndex gave you
//
// // function filterResults(filters) {
// //   var cards = document.querySelectorAll(".sd-tagged-card");
// //   console.log("filterResults(): cards found =", cards.length);
// //   if (!cards || cards.length === 0) return;
// //
// //   for (var i = 0; i < cards.length; i++) {
// //     var el = cards[i];
// //     var hide = false;
// //
// //     function fails(group) {
// //       var list = filters[group];
// //       if (!list || list.length === 0) return false;
// //
// //       for (var j = 0; j < list.length; j++) {
// //         var cls = list[j];
// //
// //         var hasClass = hasTagClass(el, cls, group);
// //
// //         if (hasClass) {
// //           if (typeof PASS_INDEX !== "undefined" && (i === 0 || i === PASS_INDEX)) {
// //             console.log(
// //               "card", i,
// //               "PASSED group", group,
// //               "via class", cls
// //             );
// //           }
// //           return false;  // passes this group
// //         }
// //
// //         // optional debug:
// //         // console.log("card", i, "does not have class", cls, el.className);
// //       }
// //
// //       if (typeof PASS_INDEX !== "undefined" && (i === 0 || i === PASS_INDEX)) {
// //         console.log(
// //           "card", i,
// //           "FAILED group", group,
// //           "needed one of", list,
// //           "but had classes:", el.className
// //         );
// //       }
// //       return true;  // failed this group
// //     }
// //     // function fails(group) {
// //     //   var list = filters[group];
// //     //   // console.log("card", i, "checking group", group, "with filter list", list);
// //     //   if (!list || list.length === 0) return false;
// //     //
// //     //   for (var j = 0; j < list.length; j++) {
// //     //     var cls = list[j];
// //     //     var hasClass =
// //     //       group === "formats"
// //     //         ? el.classList.contains(cls.toLowerCase())
// //     //         : el.classList.contains(cls);
// //     //
// //     //     if (hasClass) {
// //     //       if (i === 0 || i === PASS_INDEX) {
// //     //         console.log(
// //     //           "card", i,
// //     //           "PASSED group", group,
// //     //           "via class", cls
// //     //         );
// //     //       }
// //     //       return false;
// //     //     }
// //     //     console.log("card", i, "does not have class", cls, el.className);
// //     //   }
// //     //   if (i === 0 || i === PASS_INDEX) {
// //     //     console.log(
// //     //       "card", i,
// //     //       "FAILED group", group,
// //     //       "needed one of", list,
// //     //       "but had classes:", el.className
// //     //     );
// //     //   }
// //     //   return true;
// //     // }
// //
// //     if (fails("affiliation") ||
// //         fails("book") ||
// //         fails("published") ||
// //         fails("language") ||
// //         fails("domains") ||
// //         fails("formats") ||
// //         fails("packages")) {
// //       hide = true;
// //     }
// //
// //     if (i === 0 || i === PASS_INDEX) {
// //       console.log(
// //         "card", i,
// //         "final decision:", hide ? "HIDE" : "SHOW",
// //         "classes before:", el.className
// //       );
// //     }
// //
// //     if (hide) {
// //       el.classList.remove("d-flex");
// //       el.classList.add("d-none");
// //     } else {
// //       el.classList.remove("d-none");
// //       el.classList.add("d-flex");
// //     }
// //
// //     if (i === 0 || i === PASS_INDEX) {
// //       console.log(
// //         "card", i,
// //         "classes after:", el.className
// //       );
// //     }
// //   }
// // }
//
// function filterResults(filters) {
//   var cards = document.querySelectorAll(".sd-tagged-card");
//   console.log("filterResults(): cards found =", cards.length);
//   if (!cards || cards.length === 0) return;
//
//   var groups = [
//     "affiliation",
//     "book",
//     "published",
//     "language",
//     "domains",
//     "formats",
//     "packages"
//   ];
//
//   for (var i = 0; i < cards.length; i++) {
//     var el = cards[i];
//     var hide = false;
//
//     // Decide visibility for this card
//     for (var g = 0; g < groups.length; g++) {
//       var group = groups[g];
//       var list = filters[group];
//
//       // No filters selected for this group: no constraint
//       if (!list || list.length === 0) continue;
//
//       var matchesGroup = false;
//       for (var j = 0; j < list.length; j++) {
//         var cls = list[j];
//         if (hasTagClass(el, cls, group)) {
//           matchesGroup = true;
//           break;
//         }
//       }
//
//       // If it fails any active group, hide it
//       if (!matchesGroup) {
//         hide = true;
//         break;
//       }
//     }
//
//     // Hide/show the outer column wrapper if present, otherwise the card itself
//     var wrapper = el.closest(".sd-col") || el;
//
//     if (hide) {
//       wrapper.classList.add("d-none");
//     } else {
//       wrapper.classList.remove("d-none");
//     }
//   }
// }
//
//
// function hasTagClass(el, filter) {
//   if (!filter) return false;
//
//   // exact
//   if (el.classList.contains(filter)) return true;
//
//
//   const lower = filter.toLowerCase();
//   if (el.classList.contains(lower)) return true;
//
//   // docutils-like: strip leading non-letters, e.g. "2k-foo" -> "k-foo"
//   const normalized = lower.replace(/^[^a-zA-Z]+/, '');
//   if (normalized && el.classList.contains(normalized)) return true;
//
//   return false;
// }
//
// function clearCbs() {
//   var selectors = [
//     ".book",
//     ".affiliation",
//     ".domains",
//     ".formats",
//     ".packages",
//     ".language",
//     ".published"
//   ];
//
//   selectors.forEach(function (selector) {
//     var cbs = document.querySelectorAll(selector + " input[type='checkbox']");
//     for (var i = 0; i < cbs.length; i++) {
//       cbs[i].checked = false;
//     }
//   });
//
//   change();
// }
//
// // === INITIALIZE ON PAGE LOAD ===
// document.addEventListener("DOMContentLoaded", function () {
//   console.log("DOMContentLoaded: running init");
//
//   var bareCards = document.querySelectorAll(
//     ".sd-card.sd-sphinx-override.sd-mb-3.sd-shadow-sm.sd-card-hover.docutils"
//   );
//   console.log("init: bare .sd-card count =", bareCards.length);
//
//   for (var i = 0; i < bareCards.length; i++) {
//     var card = bareCards[i];
//     if (!card.closest(".sd-tagged-card")) {
//       console.log("init: hiding bare card", i);
//       card.style.display = "none";
//     }
//   }
//
//   var taggedCards = document.querySelectorAll(".sd-tagged-card");
//   console.log("init: tagged card count =", taggedCards.length);
//   for (var j = 0; j < taggedCards.length; j++) {
//     taggedCards[j].style.display = "";
//   }
//
//   change();
// });
//
