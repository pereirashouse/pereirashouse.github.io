(function(){
  "use strict";
  var links=window.PH_SHOP_PRODUCTS||{};
  document.querySelectorAll("[data-shop-product]").forEach(function(el){
    var key=el.getAttribute("data-shop-product");
    var url=links[key];
    if(url && /^https:\/\/[^ ]+$/i.test(url)){
      el.href=url;
      el.removeAttribute("aria-disabled");
      el.classList.remove("is-disabled");
      el.textContent=el.getAttribute("data-ready-label")||"Comprar na Shopify";
      el.setAttribute("target","_blank");
      el.setAttribute("rel","noopener");
    }else{
      el.href="#disponibilidade";
      el.setAttribute("aria-disabled","true");
      el.classList.add("is-disabled");
      el.textContent=el.getAttribute("data-pending-label")||"Disponível em breve";
    }
  });
})();
