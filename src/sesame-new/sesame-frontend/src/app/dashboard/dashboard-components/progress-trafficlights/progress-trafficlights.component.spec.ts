import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { ProgressTrafficlightsComponent } from './progress-trafficlights.component';

describe('ReferalEarningComponent', () => {
  let component: ProgressTrafficlightsComponent;
  let fixture: ComponentFixture<ProgressTrafficlightsComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ ProgressTrafficlightsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProgressTrafficlightsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
