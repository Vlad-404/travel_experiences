$(document).ready(function(){
    // Materialize sidenav
    $(".sidenav").sidenav({edge: "right"});
    // Materialize slider for the hero image
    $('.slider').slider({indicators: "true"});
    // Materialize smooth scrolling
    $('.scrollspy').scrollSpy();
    // Materialize floating action button
    $('.fixed-action-btn').floatingActionButton();
    // Materialize modal
    $('.modal').modal();
    // Materialize tooltips
    $('.tooltipped').tooltip();
    // Materialize dropdown selection (sorter)
    $('select').formSelect();
    // Materialize image enlargement
    $('.materialboxed').materialbox();

    // makes country select a mandatory entry by Tim Nelson
    // (see Acknowledgments and thank you's in readme.md)
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }

  });

// changes the image preview before uploading it
var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};