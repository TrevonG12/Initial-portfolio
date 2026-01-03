export const site = {
  name: "Trevon Griffin",
  roleTag: "Computer Science",
  gradTag: "Graduating May 2026",
  headline: "Full-Stack • Python • Backend",
  summary:
    "I build clean, deployable web applications and backend systems. I’m focused on shipping practical software, writing maintainable code, and leveling up fast through real projects.",

  about:
    "Computer Science major graduating in May 2026. I’ve built and deployed a full-stack inventory and project management app, and I’m expanding my portfolio with additional projects in data, backend, and systems to be ready for internship and entry-level opportunities.",

  email: "trevongriffin88@gmail.com",

  links: {
    resume: "#",      // put your PDF in /public/resume.pdf then set to "/resume.pdf"
    github: "https://github.com/TrevonG12",      // your GitHub
    linkedin: "https://www.linkedin.com/in/trevon-g-3b49b5231/"     // your LinkedIn
  },

  topSkills: ["Python", "Flask", "MySQL", "HTML/CSS", "Java", "Git", "Deployments"],

  quickStats: [
    { title: "Featured Project", value: "Inventory & Project Management (Deployed)" },
    { title: "Primary Stack", value: "Flask + MySQL" },
    { title: "Currently Building", value: "2–3 projects for May grad portfolio" }
  ],

  skillGroups: [
    { label: "Languages", items: ["Python", "Java", "JavaScript (basic)"] },
    { label: "Frameworks & Tools", items: ["Flask", "MySQL", "HTML", "CSS", "Git", "Railway"] }
  ],

  projects: [
    {
      title: "Inventory & Project Management System",
      tag: "Featured • Deployed",
      description:
        "A full-stack web app to manage inventory items and project workflows behind secure authentication.",
      stack: ["Python", "Flask", "DynamoDB", "HTML/CSS", "Railway"],
      bullets: [
        "Built and deployed a full-stack Flask + DynamoDB application with authentication and protected routes",
        "Designed relational schemas to store inventory and project data",
        "Implemented full CRUD features to create, update, and track items/projects",
        "Deployed to production and configured environment/database connectivity",
        "Demo User:admin Demo Password: password"
      ],
      links: {
        live: "https://inventory-project-managament-production.up.railway.app/",
        code: "#"
      }
    },
    {
  title: "Personal Portfolio Website",
  tag: "Deployed",
  description:
    "A modern, responsive portfolio built to showcase projects, skills, and experience with a clean, recruiter-friendly UI.",
  stack: ["Next.js", "TypeScript", "Tailwind CSS", "Railway"],
  bullets: [
    "Built a responsive portfolio using Next.js App Router and Tailwind CSS",
    "Created reusable UI components (navbar, project cards, badges) with TypeScript",
    "Integrated external links and static assets (resume, project demos) for sharing and recruiting",
    "Configured production builds and deployed the site to Railway"
  ],
  links: {
    live: "https://initial-portfolio-production.up.railway.app/",
    code: "https://github.com/TrevonG12/Initial-portfolio"
  }
},

    {
  title: "InsightDash (Data Analytics Dashboard)",
  tag: "Deployed",
  description:
    "Interactive data analytics dashboard built to explore sales performance, trends, and data quality.",
  stack: ["Python", "pandas", "Streamlit", "Plotly", "Railway"],
  bullets: [
    "Built an interactive dashboard with filters for date range, region, category, and channel",
    "Computed key performance indicators including revenue, orders, AOV, and refund rate",
    "Developed an Insights page highlighting top products and category performance",
    "Added a Data Quality page to validate missing values, duplicates, and business rule consistency",
    "Deployed the application for public access using Railway"
  ],
  links: {
    live: "PASTE_YOUR_RAILWAY_URL_HERE",
    code: "https://github.com/TrevonG12/Insight-Dash"
  }
},
  ],

  experience: [
    {
      title: "Tech Developer Intern",
      company: "Sponsors for Educational Opportunity",
      location: "Remote",
      dates: "Jul 2023 – Aug 2023",
      bullets: [
        "Completed 300+ hours of software engineering training focused on data structures, algorithms, and full-stack web development",
        "Designed and implemented full-stack apps using Python (Flask) and MySQL with HTML/CSS/JavaScript",
        "Collaborated in a mentorship program focused on professional growth and career readiness"
      ]
    },
    {
      title: "Web & Graphic Designer",
      company: "Campbellsville University",
      location: "Campbellsville, KY",
      dates: "Aug 2021 – Dec 2021",
      bullets: [
        "Created fundraising graphics and flyers using Adobe and Microsoft tools to support scholarship initiatives",
        "Iterated designs strategically to improve donor engagement"
      ]
    }
  ],

  education: {
    school: "Campbellsville University",
    degree: "B.S. Computer Science",
    grad: "Expected May 2026",
    courses: ["Intro to Programming (Java)", "Programming II (Java)", "Computer Concepts & Applications"]
  }
} as const;
