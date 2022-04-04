document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#failed').style.display = 'none';
    const title = document.querySelector('#recipe-name').innerHTML;

    fetch(`personalrate/${title}`)
    .then(response => response.json())
    .then(rate => {
        if (rate.value !== 0) {
            document.querySelector(`#star${rate.value}`).checked = true;
        }
    });

    button = document.querySelector('#save-recipe');
    button.addEventListener('click', function() {

        const title = document.querySelector('#recipe-name').innerHTML;
        let action = "";

        if (button.innerHTML === "Save") {
            action = "save";
        } else {
            action = "Unsave";
        }
        
        fetch(`saveRecipe/${action}`, {
            method: 'POST',
            mode: 'same-origin',
            body: JSON.stringify({
              title: title,
            })
        })
        .then(response => response.json())
        .then(result => {
            if(result.error === undefined) {
                button.innerHTML = result.status;
            }
        })
    });

    stars = document.querySelectorAll('.input-star');

    stars.forEach((star) => {
        star.addEventListener('click', () => {

            fetch(`raterecipe/${title}`, {
                method: 'POST',
                mode: 'same-origin',
                body: JSON.stringify({
                    rate: star.value,
                })
            })
            .then(response => response.json())
            .then(result => {
                if (result.error === undefined) {
                    location.reload();
                } else {
                    document.querySelector('#failed').style.display = 'block';
                    document.querySelector('#failed').innerHTML = result.error;
                }
            })
        });
      });
})
