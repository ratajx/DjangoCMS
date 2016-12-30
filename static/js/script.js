function removeComment (comment_id) {
    var csrftoken = Cookies.get('csrftoken');

    $.ajax({
        method: "POST",
        url: "/removeComment/",
        data: {id: comment_id, csrfmiddlewaretoken: csrftoken}
    }).done(function (id) {
        $("#comment_" + id).remove();
    })
};