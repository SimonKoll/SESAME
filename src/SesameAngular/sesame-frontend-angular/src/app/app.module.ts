import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { MenuComponent } from './menu/menu.component';
<<<<<<< HEAD
import { RegisterComponent } from './register/register.component';
=======
import { SettingsComponent } from './settings/settings.component';
>>>>>>> 776bca8d97a8c63f8eebce04be11f7e3b9b00e96

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    MenuComponent,
<<<<<<< HEAD
    RegisterComponent
=======
    SettingsComponent
>>>>>>> 776bca8d97a8c63f8eebce04be11f7e3b9b00e96
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
