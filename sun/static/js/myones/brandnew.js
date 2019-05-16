$(document).ready(function () {

    getfocus();

    add_products();
    add_customer_accounts();

    add_booking();
    addClickBooking();
    removeBooking();
    get_price_for_booking();


    get_price_qty_for_sale();

    removeSale();

    $("#paid").keyup(function () {
        var paid = $(this).val();
        var nettotal = $('#net_total').val();
        $("#due").val(nettotal - paid);

    });


});

// document ready fun ends


function getfocus() {
    $(function () {
        $("#name").focus();
    });
    $(function () {
        $(".pn").focus();
    });
    $(function () {
        $(".cst").focus();
    });


}

// this fuc is for adding and removing new rows in Booking form
function addClickBooking() {
    $('#addbk').click(function () {
        addNewRowBooking();
        // $(function () {
        //     $('#booking').children("tr:last").focus();
        // });

    })

}

// to remove the addl rows from form
function removeBooking() {
    $('#remove').click(function () {
        $('#booking').children("tr:last").remove();
    })
}

function addNewRowBooking() {

    $.ajax({
        url: '/add_new_booking_row/',
        type: 'get',
        dataType: 'json',
        success: function (data) {
            console.log(data.a);
            $("#booking").append(data.htmlf);
            var n = 0;
            $('.number').each(function () {
                $(this).html(++n);
            });


        }

    })

}


function get_price_for_booking() {
    $('#booking').delegate(".pid", "change", function () {
        var pid = $(this).val();

        var tr = $(this).parent().parent();

        $.ajax({
            url: '/amt_for_booking/' + pid,
            type: 'get',
            dataType: 'json',
            success: function (data) {
                var amt = data.d[0];

                console.log(data);

                tr.find(".amt").val(amt);

            }
        })
    });
    // $(function () {
    //     $("#dis").focus();
    // });

}

function add_products() {
    $('#adpro').click(function () {
        var t = $('#proform').serialize();

        $.ajax({
            url: '/add_pro/',
            method: 'POST',
            data: $('#proform').serialize(),
            success: function (data) {
                alert('Products Added.!');
                $.ajax({
                    url: '/add_pro/',
                    method: 'get',
                    success: function (data) {
                        window.location.href = '/add_pro/';


                    }
                })

            }
        })
    });
}
function add_customer_accounts() {
    $('#adcst').click(function () {
        var t = $('#cstform').serialize();

        $.ajax({
            url: '/add_cust/',
            method: 'POST',
            data: $('#cstform').serialize(),
            success: function (data) {
                alert('Customer Added.!');
                $.ajax({
                    url: '/add_cust/',
                    method: 'get',
                    success: function (data) {
                        window.location.href = '/add_cust/';


                    }
                })

            }
        })
    });
}
function add_booking() {
    $('#bookingdone').click(function () {
        var t = $('#bookingform').serialize();

        $.ajax({
            url: '/add_booking/',
            method: 'POST',
            data: $('#bookingform').serialize(),
            success: function (data) {
                alert('Booking Confirmed.!');
                $.ajax({
                    url: '/add_booking/',
                    method: 'get',
                    success: function (data) {
                        window.location.href = '/add_booking/';


                    }
                })

            }
        })
    });
}


function get_price_qty_for_sale() {
    $('#invoice_item').delegate(".pid", "change", function () {
        var pid = $(this).val();

        var tr = $(this).parent().parent();

        $.ajax({
            url: '/amt_for_sale/' + pid,
            type: 'get',
            dataType: 'json',
            success: function (data) {
                var tqty = data.d[0];
                var price = data.d[1];
                // var unt = data.d[2];
                // var bvale = data.d[3];



                tr.find(".tqty").val(tqty);

                tr.find(".price").val(price);
                tr.find(".amt").html(tr.find(".qty").val() * tr.find(".price").val());
                changeVal();
                calculate(0, 0);
            }
        })
    });

}
function changeVal() {
    $("#invoice_item").delegate(".diss", "keyup", function () {

        var dis = $(this);
        var qty = $('.qty');
        var pr = $('.price');

        var tr = $(this).parent().parent();


        var amt = qty.val()  * pr.val();
        var discount = dis.val();



        var final = amt - ((amt*discount) / 100);
        tr.find(".amt").html(final);
        calculate(0,0)








    })
}


function addClick() {
    $('#add').click(function () {
        addNewRowSale();
        changeVal();

    })
}

function changeVal() {
    $("#invoice_item").delegate(".qty", "keyup", function () {
        var qty = $(this);
        var d = $('.unit');



        if (d.val() == 'Dozen'|| d.val() == 'dozen')
        {

                var tr = $(this).parent().parent();

        tr.find(".amt").html((qty.val() * 12) * tr.find(".price").val());
        calculate(0, 0);

        }

        if (d.val() == 'Box' || d.val() == 'box'){

                var dd = $('.box');
                 var tr = $(this).parent().parent();

            tr.find(".amt").html(qty.val() * tr.find(".price").val());
                calculate(0, 0);
        }

        else
            {
             var tr = $(this).parent().parent();

        tr.find(".amt").html(qty.val()  * tr.find(".price").val());
        calculate(0, 0);
        }

    })
}
function addNewRowSale() {
    $.ajax({
        url: '/add_new_sale_row/',
        type: 'get',
        dataType: 'json',
        success: function (data) {
            //console.log(data.a);
            $("#invoice_item").append(data.htmlf);
            var n = 0;
            $('.number').each(function () {
                $(this).html(++n);
            })
        }
    })

}
function calculate(dis, paid) {
    var sub_total = 0;

    var net_total = 0;
    var discount = dis;
    var paid_amt = paid;
    var due = 0;
    $(".amt").each(function () {
        sub_total = sub_total + ($(this).html() * 1);
    })

    net_total = sub_total;
    net_total = net_total - discount;
    due = net_total - paid_amt;

    $("#sub_total").val(sub_total);

    $("#discount").val(discount);
    $("#net_total").val(net_total);
    $("#paid").val(paid_amt);
    $("#due").val(due);

}
function removeSale() {
    $('#remove').click(function () {
        $('#invoice_item').children("tr:last").remove();
    })
}