export interface Project {
  id: string;
  title: string;
  tagline: string;
  category: string;
  description: string;
  keyHighlights: string[];
  technologies: string[];
  link?: string;
  badge?: string;
}

export interface ExperienceItem {
  id: string;
  role: string;
  organization: string;
  period: string;
  domain: string;
  statusBadge?: string;
  bullets: string[];
  tags: string[];
}

export interface Certification {
  id: string;
  title: string;
  issuer: string;
  period: string;
  description: string;
  badgeColor: 'amber' | 'violet' | 'cyan' | 'gray';
}

export interface SkillCategory {
  title: string;
  subtitle: string;
  icon: string;
  skills: { name: string; level: string; percent: number }[];
}

export interface Drawing {
  id: string;
  title: string;
  subtitle: string;
  medium: string;
  hoursSpent: string;
  reflection: string;
  imageSrc: string;
  defaultLikes: number;
  tag: string;
  location: string;
}
