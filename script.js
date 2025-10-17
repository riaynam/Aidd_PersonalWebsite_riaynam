document.addEventListener('DOMContentLoaded',()=>{const y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();});
document.addEventListener('DOMContentLoaded', () => {
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  const form = document.getElementById('add-project-form');
  if (!form) return;

  const title = document.getElementById('title');
  const description = document.getElementById('description');
  const imageFileName = document.getElementById('image_file_name');
  const errors = document.getElementById('form-errors');

  function setError(field, msg) {
    field.classList.add('error');
    errors.textContent = msg;
  }
  function clearErrors() {
    errors.textContent = '';
    [title, description, imageFileName].forEach(el => el.classList.remove('error'));
  }

  form.addEventListener('submit', (e) => {
    clearErrors();
    if (!title.value.trim()) { e.preventDefault(); return setError(title, 'Title is required.'); }
    if (!description.value.trim()) { e.preventDefault(); return setError(description, 'Description is required.'); }
    if (!imageFileName.value.trim()) { e.preventDefault(); return setError(imageFileName, 'Image file name is required.'); }
    // allow normal POST submit to server
  });
});