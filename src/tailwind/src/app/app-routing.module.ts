import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { KeycloakGuard } from './keycloak.guard';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  {path: '**', component: AppComponent, canActivate:[KeycloakGuard] },
  {path: 'login', component:LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
