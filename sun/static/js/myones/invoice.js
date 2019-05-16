// $(document).ready(function () {
//     $('#add').click(function () {
//         var tqty = $("input[name=tqty]").val();
//             var qty = $("input[name=qty]").val();
//             var qty = $("input[name=price]").val();
//             var markup =
//                 "<td><b id=\"number\">1</b></td>\n" +
//                 "<td>\n" +"<select name=\"pid[]\" class=\"form-control form-control-sm\" required>\n" +
//                 "<option>Washing Machine</option>\n" +
//                 "</select>\n" +"</td>" +"<td><input name=\"tqty[]\" readonly type=\"text\" class=\"form-control form-control-sm\"></td>" +"<td><input name=\"qty[]\" type=\"text\" class=\"form-control form-control-sm\" required></td>" +"<td><input name=\"price[]\" type=\"text\" class=\"form-control form-control-sm\" readonly></td>" +"<td>Rs.1540</td> "
//
//
//
//
//
//
//
//
//
//
//             $("table #invoice_item").append(markup);
//
//
//
//
//
//     })
// })



$(document).ready(function () {
    $.ajax({
        url: '/allcustomerss/',
        type: 'get',
        dataType: 'json',

        success: function (data) {
            console.log(data.htmlf);
            $('#add').click(function () {
              $("table #invoice_item").append(data.htmlf);
              var selectedCountry = $(this).children("option:selected").val();
        console.log(selectedCountry);
        $.ajax({
            url: '/customer/' + selectedCountry,
            type: 'get',
            dataType: 'json',

            // success: function (data) {
            //     var dd = data.d
            //     console.log(dd);
            //
            //     $('input[name=tqty]').val(dd[0]);
            //     $('input[name=qty]').val(dd[1]);
            //     $('input[name=price]').val(dd[2]);





            // }
        })

            })

        }
    })
})


// this one is for getting value okay.
$(document).ready(function () {
    $('#pid').change(function () {
        $('#pid')
        var selectedCountry = $(this).children("option:selected").val();
        console.log(selectedCountry);
        $.ajax({
            url: '/customer/' + selectedCountry,
            type: 'get',
            dataType: 'json',

            success: function (data) {
                var dd = data.d
                console.log(dd);

                $('input[name=tqty]').val(dd[0]);
                $('input[name=qty]').val(dd[1]);
                $('input[name=price]').val(dd[2]);





            }
        })



    })
})




// $(document).ready(function () {
//     var btn = $('#get_order_data').click(function () {
//         alert("hahaha");
//     })
//
// })