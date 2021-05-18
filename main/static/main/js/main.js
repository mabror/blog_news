$(document).ready(function (){

    var csrfToken = $("input[name=csrfmiddlewaretoken]").val();

    $("#createButton").click(function (){
        var serializedData = $("#createForm").serialize();

        $.ajax({
            url: $("#createForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function (response) {
                alert(this.data)
            }

        })
    });
    $(".remove_link").on('click', function (e){
        e.preventDefault();
        var $this = $(this);
        if (confirm("Sure to delete?")){
            $.ajax({
                url: $this.attr("href"),
                type: "GET",
                dataType: 'json',
                success: function (resp){
                    if(resp.message === 'success'){
                        $this.parents('.post_sh').fadeOut("slow", function (){
                            $this.parents('.post_sh').remove();
                        });
                    }
                    else {
                        alert(resp.message);
                    }
                },
                error: function (resp){
                    console.log("Something went wrong")
                }
            })
        }
        return false;

    })

})
