$(document).ready(function () {
    $(".rss_delete").click(function () {
        var msg = "您真的确定要删除吗？请确认！";
        if (confirm(msg)) {
            var rss_id = $(".rss_id").val();
            console.log(rss_id)
            $.ajax({
                type: "get",
                contentType: "application/json",
                url: "/api/delete/" + rss_id,
                dataType: 'json',
                success: function (data) {
                    if (data.status == 1) {
                        window.location.reload()
                    }
                }
            });
        }
    });

    $("#update_contact-submit").click(function () {
        var msg = "您真的确定要修改吗？请确认！";
        if (confirm(msg)) {
            var source_id = $(".rss_id").val();
            var source_url = $("#update_source_url").val();
            var source_name = $("#update_source_name").val();
            var source_tag = $("#update_source_tag").val();
            var source_desc = $("#update_source_desc").val();
            var login_pd = {
                'source_id': source_id,
                'source_url': source_url,
                'source_name': source_name,
                'source_tag': source_tag,
                'source_desc': source_desc,
            };
            $.ajax({
                type: "post",
                contentType: "application/json",
                url: "/api/update" ,
                data: JSON.stringify(login_pd),
                dataType: 'json',
                success: function (data) {
                    if (data.status == 1) {
                        window.location.reload()
                    }
                }
            });
        }
    });

    $("#add_contact-submit").click(function () {
        var msg = "您真的确定要增加吗？请确认！";
        if (confirm(msg)) {
            var source_url = $("#add_source_url").val();
            var source_name = $("#add_source_name").val();
            var source_tag = $("#add_source_tag").val();
            var source_desc = $("#add_source_desc").val();
            var login_pd = {
                'source_url': source_url,
                'source_name': source_name,
                'source_tag': source_tag,
                'source_desc': source_desc,
            };
            console.log(login_pd)
            $.ajax({
                type: "post",
                contentType: "application/json",
                url: "/api/add" ,
                data: JSON.stringify(login_pd),
                dataType: 'json',
                success: function (data) {
                    if (data.status == 1) {
                        window.location.reload()
                    }
                }
            });
        }
    });

});

