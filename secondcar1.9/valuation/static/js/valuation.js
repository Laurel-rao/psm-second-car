$(document).ready(function() {
    $("#gujiaBtn").click(function() {
        $(".pop-mask").addClass("active");
        $(".pop-sell").addClass("show");
    });
    $.fn.serializeJson = function() {
        var o = {};
        var a = this.serializeArray();
        console.info(a);
        $.each(a, function() {
            if(o[this.name]) {
                if(!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return o;
    };

    $(".js-closeGujia").click(function() {
        $(".pop-mask").removeClass("active");
        $(".pop-gujia-price").removeClass("show");
        $(".pop-sell").removeClass("show");
    });
    // 省
    // $.ajaxSetup({
    //        data: {csrfmiddlewaretoken: '{{ csrf_token }}' }　});
    // $("#gj_disProvince").click(function(){
        $.ajax({
        type: "post",
        url: "ajax_province",
        dataType: "json",
        async:false,
        success: function (data) {
            // 调试数据用
            console.info(data);
            var test="";
            for (var i = 0; i < data.length; i++) {
                 var pOption = "<option value='"+data[i][0]+"'>"+data[i][1]+"</option>";
                $("#gj_disProvince").append(pOption);
                test+=pOption;
            }
            console.info(test);
            console.info($("#gj_disProvince"));
        }
    });
// });
　　　//市
     $("#gj_disProvince").change(function(){
        // $.ajaxSetup({
        //    data: {csrfmiddlewaretoken: '{{ csrf_token }}' } });
         $("#gj_disCity").attr("disabled",false);
        // $("#gj_disCity").children(":not(:first)").remove();
        $("#gj_disCity").children().remove();
        $("#gj_disCity").removeClass("disabled");
        var val=$("#gj_disProvince option:selected").val();
        // alert(val);
        $.ajax({
            type: "post",
            url: "ajax_city",
            dataType: "json",
            data: JSON.stringify({p_id:val}),
            async:false,
            success: function (data) {
                console.info(data);
                for (var i = 0; i < data.length; i++) {
                    console.info(data[i][1]);
                    var pOption = "<option value='"+data[i][0]+"'>"+data[i][1]+"</option>";
                    $("#gj_disCity").append(pOption);
                }
            }
        });
    });
     // 品牌
     // $("#gj_disbrand").click(function(){
        $.ajax({
            type: "post",
            url: "ajax_brand",
            dataType: "json",
            async:false,
            success: function (data) {
                // 调试数据用
                console.info(data);
                for (var i = 0; i < data.length; i++) {
                    console.info(data[i][1]);
                    var pOption= "<option value='"+data[i][0]+"'>"+data[i][1]+"</option>";
                    $("#gj_disbrand").append(pOption);
                }
            }
        });
    // });
　　　//车系
     $("#gj_disbrand").change(function(){
        // $.ajaxSetup({
        //    data: {csrfmiddlewaretoken: '{{ csrf_token }}' } });
         $("#gj_distag").attr("disabled",false);
        // $("#gj_disCity").children(":not(:first)").remove();
        $("#gj_distag").children().remove();
        var val=$("#gj_disbrand option:selected").val();
        // alert(val);
        $.ajax({
            type: "post",
            url: "ajax_style",
            dataType: "json",
            data: JSON.stringify({id:val}),
            success: function (data) {
                console.info(data);
                for (var i = 0; i < data.length; i++) {
                    console.info(data[i][1]);
                    var pOption = "<option value='"+data[i][0]+"'>"+data[i][1]+"</option>";
                    $("#gj_distag").append(pOption);
                }
            }
        });
    });
     //车型
     $("#gj_distag").change(function(){
        // $.ajaxSetup({
        //    data: {csrfmiddlewaretoken: '{{ csrf_token }}' } });
         $("#gj_discar").attr("disabled",false);
        // $("#gj_disCity").children(":not(:first)").remove();
        $("#gj_discar").children().remove();
        var val=$("#gj_distag option:selected").val();
        // alert(val);
        $.ajax({
            type: "post",
            url: "ajax_model",
            dataType: "json",
            data: JSON.stringify({id:val}),
            success: function (data) {
                console.info(data);
                for (var i = 0; i < data.length; i++) {
                    console.info(data[i][1]);
                    var pOption = "<option value='"+data[i][0]+"'>"+data[i][1]+"</option>";
                    $("#gj_discar").append(pOption);
                }
            }
        });
    });
     // 年份
     $("#gj_discar").change(function(){
        // $.ajaxSetup({
        //    data: {csrfmiddlewaretoken: '{{ csrf_token }}' } });
         $("#gj_disYear").attr("disabled",false);
        // $("#gj_disCity").children(":not(:first)").remove();
        $("#gj_disYear").children().remove();
        var val=$("#gj_discar option:selected").val();
        // alert(val);
        $.ajax({
            type: "post",
            url: "ajax_year",
            dataType: "json",
            data: JSON.stringify({id:val}),
            success: function (data) {
                console.info(data);
                for (var i = 0; i < data.length; i++) {
                    console.info(data[i]);
                    var pOption = "<option value='"+data[i]+"'>"+data[i]+"年"+"</option>";
                    $("#gj_disYear").append(pOption);
                }
            }
        });
    });
　　　//月份
     $("#gj_disYear").change(function(){
        // $.ajaxSetup({
        //    data: {csrfmiddlewaretoken: '{{ csrf_token }}' } });
         $("#gj_dismonth").attr("disabled",false);
        // $("#gj_disCity").children(":not(:first)").remove();
        $("#gj_dismonth").children().remove();
        var val=$("#gj_disYear option:selected").val();
        // alert(val);
        $.ajax({
            type: "post",
            url: "ajax_month",
            dataType: "json",
            data: JSON.stringify({year:val}),
            success: function (data) {
                console.info(data);
                for (var i = 0; i < data.length; i++) {
                    console.info(data[i]);
                    var pOption = "<option value='"+data[i]+"'>"+data[i]+"</option>";
                    $("#gj_dismonth").append(pOption);
                }
            }
        });
    });
     // 估价
     $("#gujiaSubmit").click(function(){
        $("#result").attr("disabled",false);
        $("#result").children().remove();
        $(".pop-sell").removeClass("show");
        $(".pop-gujia-price").addClass("show");
        var proid=$("#gj_disProvince option:selected").val();
        var cityid=$("#gj_disCity option:selected").val();
        var city =$("#gj_disCity option:selected").text();
        var modelid=$("#gj_discar option:selected").val();
        var year=$("#gj_disYear option:selected").val();
        var month=$("#gj_dismonth option:selected").text();
        var mileage=$("#gujiaRoal").val();
        var brandname = $("#gj_disbrand option:selected").text();
        var stylename = $("#gj_distag option:selected").text();
        var modelname = $("#gj_discar option:selected").text();
        var msg ={proid:proid,cityid:cityid,city:city,modelid:modelid,year:year,month:month,mileage:mileage,brandname:brandname,stylename:stylename,modelname:modelname};
        // alert(val);
        $.ajax({
            type: "post",
            url: "valuation",
            dataType: "json",
            data: JSON.stringify(msg),
            success: function (data) {
                console.info(data);
                // var reP = data['newprice']+"&nbsp"+data['vprice']+"&nbsp"+data['avgprice']+"&nbsp"+data['cityprice'];
                // $("#result").append(reP+'<br>');
                var tag=$("#gj_distag option:selected").text();
                var car=$("#gj_discar option:selected").text();
                $("#price").text(data['vprice']);
                $("#avgPrice").text(data['avgprice']);
                $("#newPrice").text(data['newprice']);
                $(".js_res_name").text(tag+" "+car);
                $(".js_res_detail").text(city+"/"+year+"年"+month+"月上牌/"+mileage+"万公里");
            }
        });
    });
});