$(document).ready(function () {
    // отслеживаем событие отправки формы
    $('#wf-form-Name').submit(function () {
        // создаем AJAX-вызов
        $.ajax({
            data: $(this).serialize(), 
            type: $(this).attr('method'),
            url: "{% url 'ajax_posting1' %}",
            success: function (response) {
                $("#wf-form-Name").replaceWith("<h1 class='heading-2 contacts' >Заявка оформлена</h1>");
            },
            error: function (response) {
                alert(response.responseJSON.errors);
                console.log(response.responseJSON.errors)
            }
        });
        return false;
    });
})
$(document).ready(function () {
    // отслеживаем событие отправки формы
    $('#email-form').submit(function () {
        // создаем AJAX-вызов
        $.ajax({
            data: $(this).serialize(), 
            type: $(this).attr('method'),
            url: "{% url 'ajax_posting2' %}",
            success: function (response) {
                $(".form-5").replaceWith("<h1 class='heading-2 contacts' >Заявка оформлена</h1>");
            },
            error: function (response) {
                alert(response.responseJSON.errors);
                console.log(response.responseJSON.errors)
            }
        });
        return false;
    });
})
function _(e) {
    var a = e.currentTarget;
    if (!(r.env("design") || window.$.mobile && /(?:^|\s)ui-link(?:$|\s)/.test(a.className))) {
      var s, l = (s = a, v.test(s.hash) && s.host + s.pathname === n.host + n.pathname ? a.hash : "");
      if ("" !== l) {
        var d = t(l);
        d.length && (e && (e.preventDefault(), e.stopPropagation()), function(t) {
          if (n.hash !== t && i && i.pushState && (!r.env.chrome || "file:" !== n.protocol)) {
            var e = i.state && i.state.hash;
            e !== t && i.pushState({
              hash: t
            }, "", t)
          }
        }(l), window.setTimeout(function() {
          ! function(e, n) {
            var r = o.scrollTop(),
              i = function(e) {
                var n = t(f),
                  r = "fixed" === n.css("position") ? n.outerHeight() : 0,
                  i = e.offset().top - r;
                if ("mid" === e.data("scroll")) {
                  var a = o.height() - r,
                    u = e.outerHeight();
                  u < a && (i -= Math.round((a - u) / 2))
                }
                return i
              }(e);
            if (r === i) return;
            var a = function(t, e, n) {
                if ("none" === document.body.getAttribute("data-wf-scroll-motion") || h.matches) return 0;
                var r = 1;
                return u.add(t).each(function(t, e) {
                  var n = parseFloat(e.getAttribute("data-scroll-time"));
                  !isNaN(n) && n >= 0 && (r = n)
                }), (472.143 * Math.log(Math.abs(e - n) + 125) - 2e3) * r
              }(e, r, i),
              s = Date.now();
            c(function t() {
              var e = Date.now() - s;
              window.scroll(0, function(t, e, n, r) {
                return n > r ? e : t + (e - t) * ((i = n / r) < .5 ? 4 * i * i * i : (i - 1) * (2 * i - 2) * (2 * i - 2) + 1);
                var i
              }(r, i, e, a)), e <= a ? c(t) : "function" == typeof n && n()
            })
          }(d, function() {
            E(d, "add"), d.get(0).focus({
              preventScroll: !0
            }), E(d, "remove")
          })
        }, e ? 0 : 300))
      }
    }
  }
var $toTop = $('.ButtonGo-up');
$(window).scroll(function() {
if ($(this).scrollTop() > 500) {
    $toTop.fadeIn();
} else if ($toTop.is(':visible')) {
    $toTop.fadeOut();
}
});
