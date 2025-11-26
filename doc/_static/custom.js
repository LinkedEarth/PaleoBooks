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
    published:   getClassOfCheckedCheckboxes(publishedCbs),
     runnable: []  // <-- add this line
  };
  console.log("Filters applied:", filters);
  filterResults(filters);
}

function getClassOfCheckedCheckboxes(checkboxes) {
  var classes = [];

  if (checkboxes && checkboxes.length > 0) {
    for (var i = 0; i < checkboxes.length; i++) {
      var cb = checkboxes[i];
      if (cb.checked) {
        classes.push(cb.getAttribute("rel"));
      }
    }
  }

  return classes;
}


function hasTagClass(el, cls, group) {
  if (!cls) return false;

  // Start from the raw filter value
  var raw = cls.toString();

  // For formats, original code used lowercase
  if (group === "formats") {
    raw = raw.toLowerCase();
  }

  // 1) Exact match
  if (el.classList.contains(raw)) return true;

  // 2) Lowercase match (just in case)
  var lower = raw.toLowerCase();
  if (el.classList.contains(lower)) return true;

  // 3) Docutils-style: strip leading non-letters (e.g. "2k-foo" -> "k-foo")
  var normalized = lower.replace(/^[^a-zA-Z]+/, "");
  if (normalized && el.classList.contains(normalized)) return true;

  return false;
}

var PASS_INDEX = 7;  // <-- replace with whatever that findIndex gave you

function filterResults(filters) {
  var cards = document.querySelectorAll(".sd-tagged-card");
  console.log("filterResults(): cards found =", cards.length);
  if (!cards || cards.length === 0) return;

  for (var i = 0; i < cards.length; i++) {
    var el = cards[i];
    var hide = false;

    function fails(group) {
      var list = filters[group];
      if (!list || list.length === 0) return false;

      for (var j = 0; j < list.length; j++) {
        var cls = list[j];

        var hasClass = hasTagClass(el, cls, group);

        if (hasClass) {
          if (typeof PASS_INDEX !== "undefined" && (i === 0 || i === PASS_INDEX)) {
            console.log(
              "card", i,
              "PASSED group", group,
              "via class", cls
            );
          }
          return false;  // passes this group
        }

        // optional debug:
        // console.log("card", i, "does not have class", cls, el.className);
      }

      if (typeof PASS_INDEX !== "undefined" && (i === 0 || i === PASS_INDEX)) {
        console.log(
          "card", i,
          "FAILED group", group,
          "needed one of", list,
          "but had classes:", el.className
        );
      }
      return true;  // failed this group
    }
    // function fails(group) {
    //   var list = filters[group];
    //   // console.log("card", i, "checking group", group, "with filter list", list);
    //   if (!list || list.length === 0) return false;
    //
    //   for (var j = 0; j < list.length; j++) {
    //     var cls = list[j];
    //     var hasClass =
    //       group === "formats"
    //         ? el.classList.contains(cls.toLowerCase())
    //         : el.classList.contains(cls);
    //
    //     if (hasClass) {
    //       if (i === 0 || i === PASS_INDEX) {
    //         console.log(
    //           "card", i,
    //           "PASSED group", group,
    //           "via class", cls
    //         );
    //       }
    //       return false;
    //     }
    //     console.log("card", i, "does not have class", cls, el.className);
    //   }
    //   if (i === 0 || i === PASS_INDEX) {
    //     console.log(
    //       "card", i,
    //       "FAILED group", group,
    //       "needed one of", list,
    //       "but had classes:", el.className
    //     );
    //   }
    //   return true;
    // }

    if (fails("affiliation") ||
        fails("book") ||
        fails("published") ||
        fails("language") ||
        fails("domains") ||
        fails("formats") ||
        fails("packages")) {
      hide = true;
    }

    if (i === 0 || i === PASS_INDEX) {
      console.log(
        "card", i,
        "final decision:", hide ? "HIDE" : "SHOW",
        "classes before:", el.className
      );
    }

    if (hide) {
      el.classList.remove("d-flex");
      el.classList.add("d-none");
    } else {
      el.classList.remove("d-none");
      el.classList.add("d-flex");
    }

    if (i === 0 || i === PASS_INDEX) {
      console.log(
        "card", i,
        "classes after:", el.className
      );
    }
  }
}

function hasTagClass(el, filter) {
  if (!filter) return false;

  // exact
  if (el.classList.contains(filter)) return true;


  const lower = filter.toLowerCase();
  if (el.classList.contains(lower)) return true;

  // docutils-like: strip leading non-letters, e.g. "2k-foo" -> "k-foo"
  const normalized = lower.replace(/^[^a-zA-Z]+/, '');
  if (normalized && el.classList.contains(normalized)) return true;

  return false;
}

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

// === INITIALIZE ON PAGE LOAD ===
document.addEventListener("DOMContentLoaded", function () {
  console.log("DOMContentLoaded: running init");

  var bareCards = document.querySelectorAll(
    ".sd-card.sd-sphinx-override.sd-mb-3.sd-shadow-sm.sd-card-hover.docutils"
  );
  console.log("init: bare .sd-card count =", bareCards.length);

  for (var i = 0; i < bareCards.length; i++) {
    var card = bareCards[i];
    if (!card.closest(".sd-tagged-card")) {
      console.log("init: hiding bare card", i);
      card.style.display = "none";
    }
  }

  var taggedCards = document.querySelectorAll(".sd-tagged-card");
  console.log("init: tagged card count =", taggedCards.length);
  for (var j = 0; j < taggedCards.length; j++) {
    taggedCards[j].style.display = "";
  }

  change();
});


// function filterResults(filters) {
//   // These are your tagged wrappers
//   var cards = document.querySelectorAll(".sd-tagged-card");
//
//   if (!cards || cards.length === 0) {
//     return;
//   }
//
//   for (var i = 0; i < cards.length; i++) {
//     var el = cards[i];
//     var hide = false;
//
//     function fails(group) {
//       var list = filters[group];
//       if (!list || list.length === 0) return false; // unconstrained
//
//       for (var j = 0; j < list.length; j++) {
//         var cls = list[j];
//         if (group === "formats") {
//           if (el.classList.contains(cls.toLowerCase())) return false;
//         } else {
//           if (el.classList.contains(cls)) return false;
//         }
//       }
//       return true;
//     }
//
//     if (fails("affiliation") ||
//         fails("book") ||
//         fails("published") ||
//         fails("language") ||
//         fails("domains") ||
//         fails("formats") ||
//         fails("packages")) {
//       hide = true;
//     }
//
//     // Override the inline style
//     el.style.display = hide ? "none" : "";
//   }
// }
//
// function clearCbs() {
//   var groups = [
//     ".book",
//     ".affiliation",
//     ".domains",
//     ".formats",
//     ".packages",
//     ".language",
//     ".published"
//   ];
//
//   groups.forEach(function (selector) {
//     var cbs = document.querySelectorAll(selector + " input[type='checkbox']");
//     for (var i = 0; i < cbs.length; i++) {
//       cbs[i].checked = false;
//     }
//   });
//
//   change();
// }
//
//
// console.log("custom.js loaded");
// document.addEventListener("DOMContentLoaded", function () {
//   change();
// });
// === FILTERING LOGIC ===
//
// // Call this when any checkbox changes
// function change() {
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
//     published:   getClassOfCheckedCheckboxes(publishedCbs)
//   };
//
//   filterResults(filters);
// }
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
// function filterResults(filters) {
//   // ⚠️ If your cards use a different wrapper class,
//   // change ".sd-tagged-card" here to whatever you see in the DOM.
//   var cards = document.querySelectorAll(".sd-tagged-card");
//
//   if (!cards || cards.length === 0) {
//     // Nothing to filter (likely the class name changed)
//     console.warn("filterResults: no elements with .sd-tagged-card found");
//     return;
//   }
//
//   // For each card, decide whether to hide it
//   for (var i = 0; i < cards.length; i++) {
//     var el = cards[i];
//     var hide = false;
//
//     // Helper: if a filter group is active, the element must have
//     // at least one of those classes. If not, we hide it.
//     function failsFilter(groupName) {
//       var group = filters[groupName];
//       if (!group || group.length === 0) {
//         return false; // no constraint from this group
//       }
//       for (var j = 0; j < group.length; j++) {
//         var cls = group[j];
//         if (el.classList.contains(cls)) {
//           return false; // passes this group
//         }
//       }
//       return true; // fails this group
//     }
//
//     if (failsFilter("affiliation") ||
//         failsFilter("book") ||
//         failsFilter("published") ||
//         failsFilter("language") ||
//         failsFilter("domains") ||
//         failsFilter("formats") ||
//         failsFilter("packages")) {
//       hide = true;
//     }
//
//     // Show or hide the card
//     el.style.display = hide ? "none" : "flex";
//   }
// }
//
// // Clear all checkboxes and reset filters
// function clearCbs() {
//   var scopes = [
//     ".book",
//     ".affiliation",
//     ".domains",
//     ".formats",
//     ".packages",
//     ".language",
//     ".published"
//   ];
//
//   scopes.forEach(function (selector) {
//     var cbs = document.querySelectorAll(selector + " input[type='checkbox']");
//     for (var i = 0; i < cbs.length; i++) {
//       cbs[i].checked = false;
//     }
//   });
//
//   change();
// }
//
// //
// // function change() {
// //
// //   var affiliationCbs = document.querySelectorAll(".affiliation input[type='checkbox']");
// //   var bookCbs = document.querySelectorAll(".book input[type='checkbox']");
// //   var langCbs = document.querySelectorAll(".language input[type='checkbox']");
// //   var domainsCbs = document.querySelectorAll(".domains input[type='checkbox']");
// //   var formatsCbs = document.querySelectorAll(".formats input[type='checkbox']");
// //   var packagesCbs = document.querySelectorAll(".packages input[type='checkbox']");
// //   var publishedCbs = document.querySelectorAll(".published input[type='checkbox']");
// //
// //   var filters = {
// //     affiliation: getClassOfCheckedCheckboxes(affiliationCbs),
// //     domains: getClassOfCheckedCheckboxes(domainsCbs),
// //     formats: getClassOfCheckedCheckboxes(formatsCbs),
// //     packages: getClassOfCheckedCheckboxes(packagesCbs),
// //     book: getClassOfCheckedCheckboxes(bookCbs),
// //     language: getClassOfCheckedCheckboxes(langCbs),
// //     published: getClassOfCheckedCheckboxes(publishedCbs)
// //
// //   };
// //
// //
// //   filterResults(filters);
// // }
// //
// // function getClassOfCheckedCheckboxes(checkboxes) {
// //   var classes = [];
// //
// //   if (checkboxes && checkboxes.length > 0) {
// //     for (var i = 0; i < checkboxes.length; i++) {
// //       var cb = checkboxes[i];
// //
// //       if (cb.checked) {
// //         classes.push(cb.getAttribute("rel"));
// //       }
// //     }
// //   }
// //
// //   return classes;
// // }
// //
// // function filterResults(filters) {
// //   var rElems = document.querySelectorAll(".sd-tagged-card");
// //   var hiddenElems = [];
// //
// //   if (!rElems || rElems.length <= 0) {
// //     return;
// //   }
// //
// //   for (var i = 0; i < rElems.length; i++) {
// //     var el = rElems[i];
// //
// //     if (filters.affiliation.length > 0) {
// //       var isHidden = true;
// //
// //       for (var j = 0; j < filters.affiliation.length; j++) {
// //         var filter = filters.affiliation[j];
// //
// //         if (el.classList.contains(filter)) {
// //           isHidden = false;
// //           break;
// //         }
// //       }
// //
// //       if (isHidden) {
// //         hiddenElems.push(el);
// //       }
// //     }
// //
// //     if (filters.book.length > 0) {
// //       var isHidden = true;
// //
// //       for (var j = 0; j < filters.book.length; j++) {
// //         var filter = filters.book[j];
// //
// //         if (el.classList.contains(filter)) {
// //           isHidden = false;
// //           break;
// //         }
// //       }
// //
// //       if (isHidden) {
// //         hiddenElems.push(el);
// //       }
// //     }
// //
// //     if (filters.published.length > 0) {
// //       var isHidden = true;
// //
// //       for (var j = 0; j < filters.published.length; j++) {
// //         var filter = filters.published[j];
// //
// //         if (el.classList.contains(filter)) {
// //           isHidden = false;
// //           break;
// //         }
// //       }
// //
// //       if (isHidden) {
// //         hiddenElems.push(el);
// //       }
// //     }
// //
// //     if (filters.runnable.length > 0) {
// //       var isHidden = true;
// //
// //       for (var j = 0; j < filters.runnable.length; j++) {
// //         var filter = filters.runnable[j];
// //
// //         if (el.classList.contains(filter)) {
// //           isHidden = false;
// //           break;
// //         }
// //       }
// //
// //       if (isHidden) {
// //         hiddenElems.push(el);
// //       }
// //     }
// //
// //     if (filters.language.length > 0) {
// //       var isHidden = true;
// //
// //       for (var j = 0; j < filters.language.length; j++) {
// //         var filter = filters.language[j];
// //
// //         if (el.classList.contains(filter)) {
// //           isHidden = false;
// //           break;
// //         }
// //       }
// //
// //       if (isHidden) {
// //         hiddenElems.push(el);
// //       }
// //     }
// //
// //     if (filters.domains.length > 0) {
// //       var isHidden = true;
// //
// //       for (var j = 0; j < filters.domains.length; j++) {
// //         var filter = filters.domains[j];
// //
// //         if (el.classList.contains(filter)) {
// //           isHidden = false;
// //           break;
// //         }
// //       }
// //
// //       if (isHidden) {
// //         hiddenElems.push(el);
// //       }
// //     }
// //
// //     if (filters.formats.length > 0) {
// //       var isHidden = true;
// //
// //       for (var j = 0; j < filters.formats.length; j++) {
// //         var filter = filters.formats[j];
// //
// //         if (el.classList.contains(filter.toLowerCase())) {
// //           isHidden = false;
// //           break;
// //         }
// //       }
// //
// //       if (isHidden) {
// //         hiddenElems.push(el);
// //       }
// //     }
// //
// //     if (filters.packages.length > 0) {
// //       var isHidden = true;
// //
// //       for (var j = 0; j < filters.packages.length; j++) {
// //         var filter = filters.packages[j];
// //
// //         if (el.classList.contains(filter)) {
// //           isHidden = false;
// //           break;
// //         }
// //       }
// //
// //       if (isHidden) {
// //         hiddenElems.push(el);
// //       }
// //     }
// //   }
// //
// //
// //
// //   for (var i = 0; i < rElems.length; i++) {
// //     rElems[i].classList.replace("d-none", "d-flex");
// //   }
// //
// //   if (hiddenElems.length <= 0) {
// //     return;
// //   }
// //
// //   for (var i = 0; i < hiddenElems.length; i++) {
// //     hiddenElems[i].classList.replace("d-flex", "d-none");
// //   }
// // }
// //
// //
// // function clearCbs() {
// //   var bookCbs = document.querySelectorAll(".book input[type='checkbox']");
// //   var affiliationCbs = document.querySelectorAll(".affiliation input[type='checkbox']");
// //   var domainsCbs = document.querySelectorAll(".domains input[type='checkbox']");
// //   var formatsCbs = document.querySelectorAll(".formats input[type='checkbox']");
// //   var packagesCbs = document.querySelectorAll(".packages input[type='checkbox']");
// //   var langCbs = document.querySelectorAll(".language input[type='checkbox']");
// //
// //   for (var i = 0; i < affiliationCbs.length; i++) {
// //     affiliationCbs[i].checked=false;
// //   }
// //
// //   for (var i = 0; i < domainsCbs.length; i++) {
// //     domainsCbs[i].checked=false;
// //   }
// //
// //   for (var i = 0; i < formatsCbs.length; i++) {
// //     formatsCbs[i].checked=false;
// //   }
// //
// //   for (var i = 0; i < packagesCbs.length; i++) {
// //     packagesCbs[i].checked=false;
// //   }
// //
// //   for (var i = 0; i < bookCbs.length; i++) {
// //     bookCbs[i].checked=false;
// //   }
// //
// //   for (var i = 0; i < langCbs.length; i++) {
// //     langCbs[i].checked=false;
// //   }
// //
// //   change();
// // }
