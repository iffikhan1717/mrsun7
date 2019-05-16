$(document).ready(function () {


    $('#invoice_item').delegate(".pid","change",function () {
        var pid = $(this).val();
        var tr = $(this).parent().parent();
        $.ajax({
            url: '/customer/' + pid,
            type: 'get',
            dataType: 'json',
            success: function (data) {
                var dd = data.d
                console.log(dd);

                tr.find(".tqty").val(dd[0]);
                tr.find(".qty").val(dd[1]);
                tr.find(".qty").val(dd[2]);
                // $('input[name=tqty]').val(dd[0]);
                // $('input[name=qty]').val(dd[1]);
                // $('input[name=price]').val(dd[2]);

            }
        })
    })

    addClick();
    removeRow();


    




})// document ready fun ends

    function addClick() {
        $('#add').click(function () {
        addNewRow();
    })
    }

    function addNewRow() {
            $.ajax({
                 url: '/allcustomerss/',
                type: 'get',
                dataType: 'json',
                success: function (data){
                     // console.log(data)
                     $("#invoice_item").append(data.htmlf);
                     var n = 0;
                     $('.number').each(function () {
                         $(this).html(++n);
                     })
                }
            })
            // getValues();
        }

    function removeRow() {
        $('#remove').click(function () {
            $('#invoice_item').children("tr:last").remove();
        })
    }



    function getValues() {
        $('.pid').change(function () {

        var selectedCountry = $(this).children("option:selected").val();
        console.log(selectedCountry);
        var tr = $(this).parent().parent();
        $.ajax({
            url: '/customer/' + selectedCountry,
            type: 'get',
            dataType: 'json',
            success: function (data) {

                console.log(data);

                tr.find(".tqty").val(data[0]);
                tr.find(".qty").val(data[1]);
                tr.find(".price").val(data[2]);
                tr.find(".total").val(data[3]);
                console.log(data[3]);
                console.log(tr.find(".amt").html());
                tr.find(".amt").html(tr.find(".qty").val() * tr.find(".price").val())


            }
        })
            })
    }

    $("#invoice_item").delegate(".qty","keyup",function(){
		var qty = $(this);
		var tr = $(this).parent().parent();
		if (isNaN(qty.val())) {
			alert("Please enter a valid quantity");
			qty.val(1);
		}else{
			if ((qty.val() - 0) > (tr.find(".tqty").val()-0)) {
				alert("Sorry ! This much of quantity is not available");
				aty.val(1);
			}else{
				tr.find(".amt").html(qty.val() * tr.find(".price").val());
				calculate(0,0);
			}
		}

	})