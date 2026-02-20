document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Toggle
  const navBtn = document.querySelector('.nav-mobile-btn');
  const navLinks = document.querySelector('.nav-links');

  if (navBtn && navLinks) {
    navBtn.addEventListener('click', () => {
      navLinks.classList.toggle('active');
      navBtn.innerHTML = navLinks.classList.contains('active') ? '✕' : '☰';
    });
  }

  // Set default current date to next Saturday if possible on order form
  const dateDropdown = document.getElementById('pickup-date');
  if (dateDropdown) {
    const today = new Date();
    // Options: Feb 21, Feb 28, Mar 7 (2026)
    // We just leave the first option as default since the list is small.
  }

  // Order Form Handle
  const orderForm = document.getElementById('order-form');
  const copyBtn = document.getElementById('copy-btn');
  const mailtoBtn = document.getElementById('mailto-btn');
  const copyFeedback = document.getElementById('copy-feedback');

  if (orderForm) {
    function generateEmailBody() {
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const phone = document.getElementById('phone').value;
      const request = document.getElementById('request').value;
      const date = document.getElementById('pickup-date').value;
      const notes = document.getElementById('notes').value;

      return `Order Request for ${date}\n\n` +
             `Name: ${name}\n` +
             `Email: ${email}\n` +
             `Phone: ${phone}\n\n` +
             `Requested Items:\n${request}\n\n` +
             `Notes/Allergies:\n${notes}\n`;
    }

    mailtoBtn.addEventListener('click', (e) => {
      if (!orderForm.checkValidity()) {
        orderForm.reportValidity();
        e.preventDefault();
        return;
      }
      const body = encodeURIComponent(generateEmailBody());
      const subject = encodeURIComponent(`Order Request from ${document.getElementById('name').value}`);
      window.location.href = `mailto:mariannemurry@gmail.com?subject=${subject}&body=${body}`;
    });

    copyBtn.addEventListener('click', () => {
      if (!orderForm.checkValidity()) {
        orderForm.reportValidity();
        return;
      }
      const textToCopy = generateEmailBody();
      navigator.clipboard.writeText(textToCopy).then(() => {
        copyFeedback.style.display = 'block';
        setTimeout(() => {
          copyFeedback.style.display = 'none';
        }, 3000);
      });
    });
  }
});
