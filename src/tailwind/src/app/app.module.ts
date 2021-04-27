import { APP_INITIALIZER, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { KeycloakAngularModule, KeycloakService } from 'keycloak-angular';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { EntrylistComponent } from './entrylist/entrylist.component';
import { AddUserComponent } from './add-user/add-user.component';
import { SettingsComponent } from './settings/settings.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { StreamComponent } from './stream/stream.component';

function initializeKeycloak(keycloak: KeycloakService) {
  return () =>
    keycloak.init({
      config: {
        url: 'http://192.168.0.146:8180/auth',
        realm: 'sesame-realm',
        clientId: 'sesame-web-app',
      },
      initOptions: {
        onLoad: 'check-sso',
        silentCheckSsoRedirectUri:
          window.location.origin + '/assets/silent-check-sso.html',
      },
    });
}
@NgModule({
  declarations: [
    AppComponent,
    EntrylistComponent,
    AddUserComponent,
    SettingsComponent,
    LoginComponent,
    HomeComponent,
    StreamComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    KeycloakAngularModule
  ],
  providers: [{
    provide: APP_INITIALIZER,
    useFactory: initializeKeycloak,
    multi: true,
    deps: [KeycloakService],
  },],
  bootstrap: [AppComponent]
})
export class AppModule { }
