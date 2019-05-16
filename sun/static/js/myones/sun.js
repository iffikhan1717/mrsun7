$(document).ready(function () {

    getfocus();

    add_products();
    add_customer_accounts();

    add_booking();
    addClickBooking();
    removeBooking();
    get_price_for_booking();
    discount_for_booking();

    add_sale();
    get_discount();
    addClick();
    get_price_qty_for_sale();

    add_exp();
    transfer_debit();
    update_account();

    get_discount_pro();

    update_account_com();

    get_bills_sale();

    get_debt_bills();

    get_payment_bills();

    get_discount_china();

    purchase();

    get_rate_tt();

    add_sale_return();

    paying_salary();

    addClickpur();

    get_bills_pur();

    $("#paid").keyup(function () {
        var paid = $(this).val();
        var nettotal = $('#net_total').val();
        $("#due").val(nettotal - paid);

    });




});


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
                        window.location.href = '/booking_invoice/';


                    }
                })

            }
        })
    });
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
function addClickBooking() {
    $('#addbk').click(function () {
        addNewRowBooking();
        get_price_for_booking();
    })

}
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
function discount_for_booking() {
    $('#booking').delegate(".diss", "change", function () {

        var dis = $(this).val();

        alert(dis);
        var tr = $(this).parent().parent();

        var p = tr.find(".amt").val();
        var q = tr.find(".qty").val();
        var pp = p * q;
        alert(pp);

        tr.find(".total").val(pp - ((pp*dis)/100));


    })
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


function add_sale() {
    $('#order_form').click(function () {
        alert('i am order');
        var t = $('#get_order_data').serialize();

        $.ajax({
            url: '/add/sale/',
            method: 'POST',
            data: $('#get_order_data').serialize(),
            success: function (data) {
                alert('Saled Confirmed.!');
                $.ajax({
                    url: '/add/sale/',
                    method: 'get',
                    success: function (data) {
                        window.location.href = '/sales_invoice/';


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
                var cod = data.d[2];




                tr.find(".tqty").val(tqty);

                tr.find(".price").val(price);
                tr.find(".ec").val(cod);
                tr.find(".amt").html(tr.find(".qty").val() * tr.find(".price").val());

                changeVal();

                calculate(0, 0);


            }
        })
    });

}
function get_discount() {
    $('#invoice_item').delegate(".diss", "change", function () {
        var dis = $(this).val();

        var tr = $(this).parent().parent();

        var t = tr.find(".amt").html();

        alert(dis);
        alert(t);
        tr.find(".amt").html(t - ((t * dis)/100));
        calculate(0, 0);





    });

}

function get_discount_pro() {
    $('#myamountform').delegate(".rss", "change", function () {
        var rss = $(this).val();
        alert('working');


        var t = $('.rmb').val();

        $('.myamt').val(rss * t);






    });

}



function addClick() {
    $('#add').click(function () {
        addNewRow();
        changeVal();
        removeRow();


    })
}
function changeVal() {
    $("#invoice_item").delegate(".qty", "keyup", function () {
        var qty = $(this);


        var tr = $(this).parent().parent();


        tr.find(".amt").html(qty.val()  * tr.find(".price").val());
        calculate(0, 0);


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
function addNewRow() {
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
function removeRow() {
    $('#remove').click(function () {
        $('#invoice_item').children("tr:last").remove();
        calculate(0, 0);
    })

}



function add_exp() {
    $('#addexp').click(function () {
        alert('yes');
        var inv = $('#myamountform').serialize();
        $.ajax({
            url: '/add_expensess/',
            method: 'POST',
            data: $('#myamountform').serialize(),
            success: function (data) {
                alert('Expense Added...!');
                window.location.href = '/add_expensess/';

            }
        })
    })

}
function transfer_debit() {
    $('#trans-done').click(function () {
        alert('yes');
        var inv = $('#myamountform').serialize();
        $.ajax({
            url: '/transfer_debit/',
            method: 'POST',
            data: $('#myamountform').serialize(),
            success: function (data) {
                alert('Accounts Updated...!');
                window.location.href = '/transfer_debit/';

            }
        })
    })

}



function update_account() {
    $('#amount-done').click(function () {
        alert('okay');
        var inv = $('#myamountform1').serialize();
        $.ajax({
            url: '/add_amount_page/',
            method: 'POST',
            data: $('#myamountform1').serialize(),
            success: function (data) {
                alert('Accounts Updated...!');
                window.location.href = '/debit_rep/';

            }
        })
    })

}

function update_account_com() {
    $('#amount-donecom').click(function () {
        alert('okay paying come');
        var inv = $('#myamountform1').serialize();
        $.ajax({
            url: '/add_amount_page_com/',
            method: 'POST',
            data: $('#myamountform1').serialize(),
            success: function (data) {
                alert('Accounts Updated...!');
                window.location.href = '/payment_rep/';

            }
        })
    })

}


function get_bills_sale() {
    $('.my').click(function () {
        var sid = $('#txt').val();


        $.ajax({
            success: function (data) {
                window.location.href = '/bills/' + sid;
            }
        })
    });

}


function get_debt_bills() {
    $('.dbtn').click(function () {
        var sid = $('#debt').val();


        $.ajax({
            success: function (data) {
                window.location.href = '/debit_rep/' + sid;
            }
        })
    });

}


function get_payment_bills() {
    $('.pbtn').click(function () {
        var sid = $('#pay').val();


        $.ajax({
            success: function (data) {
                window.location.href = '/payment_rep/' + sid;
            }
        })
    });

}


function get_discount_china() {
    $('#purchase').delegate(".ps", "change", function () {
        var pss = $(this).val();
        alert('pur working new');

        var tr = $(this).parent().parent();

        var t = tr.find('.chi').val();

        tr.find('.rp').val(t -(t * pss)/100);

        // $('.rp').val(t -(t * pss)/100);






    });

}

function get_rate_tt() {
    $('#purchase').delegate(".qty", "change", function () {
        var qty = $(this).val();
        alert('pur working new');

        alert(qty);

        var tr = $(this).parent().parent();

        var t = tr.find('.rp').val();
        alert(t);

        tr.find('.ttt').val(qty * t);






    });

}






function purchase() {
    $('#prbtn').click(function () {
        alert('okay purchase');
        var inv = $('#purchase').serialize();
        $.ajax({
            url: '/add_purchase/',
            method: 'POST',
            data: $('#purchase').serialize(),
            success: function (data) {
                alert('purchase Done...!');
                window.location.href = '/pur_invoice/';

            }
        })
    })

}


function add_sale_return() {
    $('#order_formreturn').click(function () {
        alert('i am order return');
        var t = $('#get_order_data').serialize();

        $.ajax({
            url: '/add/sale_return/',
            method: 'POST',
            data: $('#get_order_data').serialize(),
            success: function (data) {
                alert('Saled return Confirmed.!');
                $.ajax({
                    url: '/add/sale_return/',
                    method: 'get',
                    success: function (data) {
                        window.location.href = '/sales_invoice_return/';


                    }
                })

            }
        })
    });
}



function paying_salary() {
    $('#sal').click(function () {
        alert('salworking');
        var s = $('#salform').serialize();
        $.ajax({
            url: '/give_salary/',
            method: 'POST',
            data: $('#salform').serialize(),
            success: function (data) {
                alert('Salary Paid');
                window.location.href = '/give_salary/';

            }
        })
    })

}

function addNewRowpur() {

    $.ajax({
        url: '/add_new_pur_row/',
        type: 'get',
        dataType: 'json',
        success: function (data) {
            console.log(data.a);
            $("#pur").append(data.htmlf);



        }

    })

}
function addClickpur() {
    $('#nwrow').click(function () {
        addNewRowpur();

    })

}

function get_bills_sale() {
    $('.my').click(function () {
        var sid = $('#txt').val();


        $.ajax({
            success: function (data) {
                window.location.href = '/bills/' + sid;
            }
        })
    });

}
function get_bills_pur() {
    $('.my').click(function () {
        var sid = $('#txt').val();


        $.ajax({
            success: function (data) {
                window.location.href = '/s_pur_bills/' + sid;
            }
        })
    });

}
