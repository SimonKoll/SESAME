import { Routes } from '@angular/router';

import { EntryComponent } from './entry/entry.component';
import { LiveComponent } from './live/live.component';
import { ProfileComponent } from './profile/profile.component';
import { AccessmanagementComponent } from './access-management/accessmanagement.component';

export const ComponentsRoutes: Routes = [
	{
		path: '',
		children: [

			{
				path: 'live',
				component: LiveComponent,
				data: {
					title: 'Live'
				}
			},
			{
				path: 'entry',
				component: EntryComponent,
				data: {
					title: 'Entries'
				}
			},
			{
				path: 'profile',
				component: ProfileComponent,
				data: {
					title: 'Profile'
				}
			},
			{
				path: 'accessmanagement',
				component: AccessmanagementComponent,
				data: {
					title: 'Access Management'
				}
			}
		]
	}
];
