const services = [
  {
    title: 'E-Commerce',
    icon: '🛍️',
    description: 'Luxury storefronts, smart carts, and personalized recommendations.',
    features: ['High-conversion product pages', 'Wishlist and loyalty', 'Fast checkout flow']
  },
  {
    title: 'Digital Seva',
    icon: '📱',
    description: 'Government and citizen service access with modern digital convenience.',
    features: ['Online form assistance', 'Smart appointment booking', 'Transparent status tracking']
  },
  {
    title: 'Food Delivery',
    icon: '🍜',
    description: 'Fast ordering, live tracking, and premium dining experiences.',
    features: ['Live order tracking', 'Chef recommendations', 'Express delivery']
  },
  {
    title: 'Taxi & Rides Booking',
    icon: '🚕',
    description: 'Reliable transportation booking with real-time availability.',
    features: ['Instant ride matching', 'Fare estimates', 'Route optimization']
  },
  {
    title: 'Beauty Academy',
    icon: '💄',
    description: 'High-end beauty learning, course booking, and skill growth.',
    features: ['Live workshop access', 'Certified mentors', 'Course bundles']
  },
  {
    title: 'Marketplace',
    icon: '🏪',
    description: 'Multi-vendor commerce with a polished seller and buyer experience.',
    features: ['Vendor dashboards', 'Secure payouts', 'Promoted listings']
  },
  {
    title: 'Health & Wellness',
    icon: '🧘',
    description: 'Personal wellness journeys, consultations, and recovery services.',
    features: ['Doctor booking', 'Wellness subscriptions', 'Care reminders']
  },
  {
    title: 'NGO',
    icon: '🤝',
    description: 'Community impact tools with donation flows and volunteer coordination.',
    features: ['Donation campaigns', 'Volunteer onboarding', 'Impact reports']
  },
  {
    title: 'AI Automation',
    icon: '🤖',
    description: 'Automation tools that reduce friction and save valuable time.',
    features: ['Workflow bots', 'Smart replies', 'Analytics automation']
  },
  {
    title: 'Real Estate',
    icon: '🏡',
    description: 'Property discovery with refined search and guided buying support.',
    features: ['Virtual tours', 'Agent chat', 'Saved property lists']
  },
  {
    title: 'Job Search',
    icon: '💼',
    description: 'Modern hiring marketplace with role matching and candidate insights.',
    features: ['Smart matching', 'Application tracking', 'Resume AI support']
  },
  {
    title: 'Website & App Development',
    icon: '💻',
    description: 'Custom digital products tailored for premium brands and startups.',
    features: ['Product strategy', 'UX/UI systems', 'Launch support']
  }
];

const serviceGrid = document.getElementById('serviceGrid');
const searchInput = document.getElementById('serviceSearch');
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.getElementById('navLinks');
const demoForm = document.getElementById('demoForm');
const formMessage = document.getElementById('formMessage');

function renderServices(filter = '') {
  const query = filter.trim().toLowerCase();
  const visible = services.filter((service) => {
    const haystack = `${service.title} ${service.description} ${service.features.join(' ')}`.toLowerCase();
    return haystack.includes(query);
  });

  serviceGrid.innerHTML = visible
    .map(
      (service) => `
        <article class="service-card">
          <div class="card-icon">${service.icon}</div>
          <h3>${service.title}</h3>
          <p>${service.description}</p>
          <ul>
            ${service.features.map((item) => `<li>${item}</li>`).join('')}
          </ul>
        </article>
      `
    )
    .join('');
}

searchInput.addEventListener('input', (event) => renderServices(event.target.value));
renderServices();

if (menuToggle && navLinks) {
  menuToggle.addEventListener('click', () => navLinks.classList.toggle('open'));

  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => navLinks.classList.remove('open'));
  });
}

if (demoForm && formMessage) {
  demoForm.addEventListener('submit', (event) => {
    event.preventDefault();
    formMessage.textContent = 'Thank you — your premium demo request has been received.';
    demoForm.reset();
  });
}

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').catch(() => {});
  });
}
