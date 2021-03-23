import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfilepicUsernameComponent } from './profilepic-username.component';

describe('ProfilepicUsernameComponent', () => {
  let component: ProfilepicUsernameComponent;
  let fixture: ComponentFixture<ProfilepicUsernameComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProfilepicUsernameComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfilepicUsernameComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
