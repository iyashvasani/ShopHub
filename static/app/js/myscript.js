$('#slider1, #slider2, #slider3, #slider4, #slider5, #slider6, #slider7, #slider8, #slider9, #slider10, #slider11, #slider12, #slider13').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function () {
    // console.log('click');
    var id = $(this).attr('pid').toString();
    // console.log(id);
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            // console.log(data);
            // console.log("success");
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})


$('.minus-cart').click(function () {
    // console.log('click');
    var id = $(this).attr('pid').toString();
    // console.log(id);
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function (data) {
            // console.log(data);
            // console.log("success");
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})



$('.remove-cart').click(function () {
    // console.log('click');
    var id = $(this).attr('pid').toString();
    // console.log(id);
    var eml = this
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function (data) {
            // console.log(data);
            // console.log("Delete");
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})

function alert_msg() {
    document.getElementById("alert");
    alert("Order Placed Succuessfully!");
}