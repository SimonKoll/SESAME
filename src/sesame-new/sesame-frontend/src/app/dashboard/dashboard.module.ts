import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';
import { ChartsModule } from 'ng2-charts';
import { DashboardComponent } from './dashboard.component';
import { SalesratioGraphComponent } from './dashboard-components/livestream-preview/salesratio-graph.component';
import { LatestSalesComponent } from './dashboard-components/unknown-entry-tries/latest-sales.component';
import { ReferalEarningComponent } from './dashboard-components/progress-trafficlights/referal-earning.component';
import { UsersComponent } from './dashboard-components/entries/users.component';
import { MatTableModule } from '@angular/material/table';

const routes: Routes = [
	{
		path: '',
		data: {
			title: 'Sesame - Dashboard'
		},
		component: DashboardComponent
	}
];

@NgModule({
	imports: [FormsModule, CommonModule, RouterModule.forChild(routes), ChartsModule,  MatTableModule],
	declarations: [
		DashboardComponent,
		SalesratioGraphComponent,
		LatestSalesComponent,
		ReferalEarningComponent,
		UsersComponent
	]
})

export class DashboardModule {}
