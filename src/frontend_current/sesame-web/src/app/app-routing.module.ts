import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { NavComponent } from './nav/nav.component';
import { RegisterComponent } from './register/register.component';
import { AppAuthGuard } from '../app-auth-guard.guard';
import { HomeComponent } from './home/home.component'
import { LiveComponent } from './live/live.component'

const routes: Routes = [
  {path: "home", component: LoginComponent},
  { path: '',   redirectTo: '/home', pathMatch: 'full' }
];
const appRoutes: Routes = [
  { 
    path: 'live', 
    loadChildren: () =>  LiveComponent,
    canActivate: [AppAuthGuard], 
    data: { roles: ['Owner'] }
  },
  { 
    path: 'home', 
    loadChildren: () => HomeComponent,
    canActivate: [AppAuthGuard], 
    data: { roles: ['Owner', 'Entrant'] }
  },
...

 ];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers:[AppAuthGuard]
})
export class AppRoutingModule { }
