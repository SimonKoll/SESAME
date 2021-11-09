import { RouteInfo } from './sidebar.metadata';

export const ROUTES: RouteInfo[] = [
  {
    path: '/dashboard',
    title: 'Dashboard',
    icon: 'mdi mdi-gauge',
    class: '',
    extralink: false,
    submenu: []
  },
  {
    // path: '/component/accordion',
    path: '',
    title: 'Entries',
    icon: 'mdi mdi-equal',
    class: '',
    extralink: false,
    submenu: []
  },
  {
    path: '',
    title: 'Live',
    icon: 'mdi mdi-message-bulleted',
    class: '',
    extralink: false,
    submenu: []
  },
  {
    path: '',
    title: 'Access Management',
    icon: 'mdi mdi-view-carousel',
    class: '',
    extralink: false,
    submenu: []
  }
];
