import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';
import { ChartsModule } from 'ng2-charts';
import { DashboardComponent } from './dashboard.component';
import { LivestreamPreviewComponent } from './dashboard-components/livestream-preview/livestream-preview.component';
import { UnknownEntryTriesComponent } from './dashboard-components/unknown-entry-tries/unknown-entry-tries.component';
import { ProgressTrafficlightsComponent } from './dashboard-components/progress-trafficlights/progress-trafficlights.component';
import { EntriesListComponent } from './dashboard-components/entries-list/entries-list.component';
import { MatTableModule } from '@angular/material/table';

const routes: Routes = [
	{
		path: '',
		data: {
			title: 'Dashboard'
		},
		component: DashboardComponent
	}
];

@NgModule({
	imports: [FormsModule, CommonModule, RouterModule.forChild(routes), ChartsModule,  MatTableModule],
	declarations: [
		DashboardComponent,
		LivestreamPreviewComponent,
		UnknownEntryTriesComponent,
		ProgressTrafficlightsComponent,
		EntriesListComponent
	]
})

export class DashboardModule {}
