from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150, help_text="e.g. Full-Stack Developer & Data Engineer")
    tagline = models.CharField(max_length=255, help_text="Short hero subtitle")
    about = models.TextField(help_text="About section body text")
    email = models.EmailField()
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    resume_file = models.FileField(upload_to='resume/', blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    hero_cta_label = models.CharField(max_length=50, default="View My Work")

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Languages, Frameworks, Tools")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, help_text="Devicon class e.g. devicon-python-plain")
    proficiency = models.PositiveIntegerField(default=80, help_text="0-100")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated: Python, Django, React")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Experience(models.Model):
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if current")
    description = models.TextField(help_text="One bullet point per line")
    company_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} @ {self.company}"

    @property
    def is_current(self):
        return self.end_date is None

    @property
    def date_range(self):
        start = self.start_date.strftime("%b %Y")
        end = "Present" if self.is_current else self.end_date.strftime("%b %Y")
        return f"{start} – {end}"

    def bullet_points(self):
        return [line.strip() for line in self.description.splitlines() if line.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"{self.name} — {self.subject}"
