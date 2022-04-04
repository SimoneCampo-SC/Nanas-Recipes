document.addEventListener('DOMContentLoaded', function () {

  document.querySelector('#failed').style.display = 'none';
  document.querySelector('#success').style.display = 'none';

  // Add new recipe
  document.querySelector('#recipe-form').onsubmit = function () {
    const title = document.querySelector('#name').value;
    const image = document.querySelector('#image').value;
    const category = document.querySelector('#category').value;
    const difficulty = document.querySelector('#difficulty').value;
    const cost = document.querySelector('#cost').value;
    const time = document.querySelector('#time').value;
    const ingredients = document.querySelector('#ingredients').value;
    const description = document.querySelector('#description').value;
    const preparation = document.querySelector('#preparation').value;
    const tips = document.querySelector('#tips').value;
    
    if (document.querySelector('.sec-name').innerHTML === "New Recipe") {
      fetch('postRecipe', {
        method: 'POST',
        body: JSON.stringify({
          title: title,
          image: image,
          category: category,
          difficulty: difficulty,
          cost: cost,
          time: time,
          ingredients: ingredients,
          description: description,
          preparation: preparation,
          tips: tips
        })
      })
      .then(response => response.json())
      .then(result => {
        if (result.message !== undefined) {
          document.querySelector('#name').value = '';
          document.querySelector('#image').value = '';
          document.querySelector('#category').value = '';
          document.querySelector('#difficulty').value = '';
          document.querySelector('#cost').value = '';
          document.querySelector('#time').value = '';
          document.querySelector('#ingredients').value = '';
          document.querySelector('#description').value = '';
          document.querySelector('#preparation').value = '';
          document.querySelector('#tips').value = '';
          document.querySelector('#failed').style.display = 'none';
          document.querySelector('#success').style.display = 'block';
          document.querySelector('#success').innerHTML = result.message;
        } else {
          document.querySelector('#success').style.display = 'none';
          document.querySelector('#failed').style.display = 'block';
          document.querySelector('#failed').innerHTML = result.error;
        }
      });
    } else {
      const id = parseInt(document.querySelector('#recipe-id').innerHTML);
      fetch(`editRecipe/${id}`, {
        method: 'POST',
        mode: 'same-origin',
        body: JSON.stringify({
          title: title,
          image: image,
          category: category,
          difficulty: difficulty,
          cost: cost,
          time: time,
          ingredients: ingredients,
          description: description,
          preparation: preparation,
          tips: tips
        })
      })
      .then(response => response.json())
      .then(result => {
        if (result.message !== undefined) {
          var div_list = document.querySelectorAll('.form-group'); // returns NodeList
          var div_array = [...div_list]; // converts NodeList to Array
          div_array.forEach(div => { div.style.display = 'none';})
          
          document.querySelector('#failed').style.display = 'none';
          document.querySelector('#success').style.display = 'block';
          document.querySelector('#success').innerHTML = result.message;

        } else {
          document.querySelector('#success').style.display = 'none';
          document.querySelector('#failed').style.display = 'block';
          document.querySelector('#failed').innerHTML = result.error;
        }
      }) 
    } 
    return false;
  } 
})