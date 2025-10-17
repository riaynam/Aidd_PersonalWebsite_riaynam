document.addEventListener('DOMContentLoaded',()=>{const y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();});
document.addEventListener('DOMContentLoaded', () => {
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  const form = document.getElementById('contact-form');
  if (!form) return;

  const email = document.getElementById('email');
  const pwd = document.getElementById('password');
  const cpwd = document.getElementById('confirmPassword');
  const first = document.getElementById('firstName');
  const last = document.getElementById('lastName');
  const errors = document.getElementById('form-errors');

  function setError(field, msg) {
    field.classList.add('error');
    errors.textContent = msg;
  }
  function clearErrors() {
    errors.textContent = '';
    [email,pwd,cpwd,first,last].forEach(el => el.classList.remove('error'));
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    clearErrors();

    if (!first.value.trim()) return setError(first, 'First Name is required.');
    if (!last.value.trim()) return setError(last, 'Last Name is required.');

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email.value)) return setError(email, 'Enter a valid email address.');

    if (pwd.value.length < 8) return setError(pwd, 'Password must be at least 8 characters.');
    if (pwd.value !== cpwd.value) return setError(cpwd, 'Passwords must match.');

    // Passed client validation — simulate submit then redirect
    window.location.href = 'thankyou.html';
  });
});