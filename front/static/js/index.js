//轮播
$(()=>{
    $(()=>{
        var LIWIDTH=1300,timer=null,moved=0,duration=500,wait=3000;
        var $ul=$("ul.sub-img"); //图片列表
        $ul.css("width",LIWIDTH*5);
        var $ulCase=$("ul.sub-case");//小方块
        $ulCase.children().first().addClass("sub-active");
        function move(){
            $ul.animate({
                left:-LIWIDTH*moved
            },duration,function(){
                if(moved==4){
                    moved=0;
                    $ul.css("left",0);
                }
                $ulCase.children(`:eq(${moved})`).addClass("sub-active")
                    .siblings().removeClass("sub-active");
            })
        }
        timer=setInterval(()=>{
            moved++;
            move();
        },wait+duration);
        //方块鼠标移入事件
        $ulCase.on("mouseenter","li",e=>{
            moved=$(e.target).index();
            //防止动画叠加
            clearInterval(timer);
            $ul.stop(true);//停止当前动画
            move();
        });
        //鼠标移入停止定时器，移出启动定时器
        $(".sub-img").hover(
            ()=>{clearInterval(timer)},
            ()=>{
                timer=setInterval(()=>{
                    moved++;
                    move();
                },wait+duration)
            }
        );
    })
});

// 登录跳转
// $(()=>{
//     $(".btn-login").click((e)=>{
//         e.preventDefault();
//         $(location).attr("href","login.html");
//     })
// });