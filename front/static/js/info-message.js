$(()=>{
    var move=0;
    var $point=$(".point");
    var $form=$(".contain>.form");
    //点击下一步
    $(".next").click((e)=>{
        $tar=$(e.target);
        move++;//1
        $(".prev").removeAttr("disabled");//move大于1的时候  上一页可用
        //小于move的变成绿色
        $point.children(`:lt(${move})`).find("b").css("background-color","#10C642")
        //等于move的变成橙色
        $point.children(`:eq(${move})`).find("b").css("background-color","#FF8F03")
        console.log(move);

//         function check() {
//             var radio = document.getElementsByName("gender")
//     for(i=0;i<radio.length;i++){
//         if(radio[i].checked){
//             return radio[i].value
//         }
//     }
// }
// var radio = document.getElementsByName("gender").innerHTML = check();
//
//
// function service() {
//     var service = document.getElementsByName("isService")
//     for(i=0;i<service.length;i++){
//         if(service[i].checked){
//             return service[i].value
//         }
//     }
// }
//
// var service = document.getElementsByName("isService").innerHTML = service();
//
//
// function formalities() {
//     var formalities = document.getElementsByName("formalities")
//     for(i=0;i<formalities.length;i++){
//         if(formalities[i].checked){
//             return formalities[i].value
//         }
//     }
// }
//
// var formalities = document.getElementsByName("formalities").innerHTML = formalities();
//
// function debt() {
//     var debt = document.getElementsByName("isDebt")
//     for(i=0;i<debt.length;i++){
//         if(debt[i].checked){
//             return debt[i].value
//         }
//     }
// }
// var debt = document.getElementsByName("isDebt").innerHTML = debt();
// var brandstext = $("#brands").find("option:selected").text();

// function setImgName(basicfile){
// document.getElementById("blogrollimagename").value=basicfile.value;
// }



        if(move==4){
               $tar.html("提交");
            // $tar.attr('id','sub').html("提交").click(function(){
            //    // $.post('/user/infomesin','aaa.html');
            //     $.ajax({
            //         url:"/user/infomesin/",
            //         type:"POST",
            //         // processData : false,
            //         // contentType : false,
            //         fileElementId:'pic',
            //         data:{
            //             "realname": $("#realname").val(),
            //             "identity": $("#identity").val(),
            //             "address": $("#address").val(),
            //             "uphone": $("#uphone").val(),
            //             "sex": radio,
            //             "brands": brandstext,
            //             "model": $("#model").val(),
            //             "regist_date": $("#regist_date").val(),
            //             "engineNo": $("#engineNo").val(),
            //             "mileage":$("#mileage").val(),
            //             "isService": service,
            //             "price": $("#price").val(),
            //             "newprice": $("#newprice").val(),
            //             // "picture": $("#pic").val(),
            //             "formalities": formalities,
            //             "debt": debt,
            //             "promise": $("#promise").val(),
            //
            //         },
            //         // async:false,
            //     })
            //
            // })
        }else if(move==5){
            $tar.attr("type","submit")
        }
        $form.children(`div:eq(${move})`).css("display","block").siblings("div").css("display","none");
    });
    
    //点击上一步
    $(".prev").click((e)=>{
        $tar=$(e.target);
        move--;
        if(move<=0){//move小于或者等于0时，上一页不可用
            $tar.attr("disabled",true);
        }
        $(".next").html("下一步");
        $point.children(`:gt(${move})`).find("b").css("background-color","#DEDCD8");
        $point.children(`:eq(${move})`).find("b").css("background-color","#FF8F03");
        $form.children(`div:eq(${move})`).css("display","block").siblings("div").css("display","none");
        console.log(move);
    })
})





