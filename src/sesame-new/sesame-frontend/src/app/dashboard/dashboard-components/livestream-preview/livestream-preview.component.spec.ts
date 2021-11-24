import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { LivestreamPreviewComponent } from './livestream-preview.component';

describe('SalesratioGraphComponent', () => {
  let component: LivestreamPreviewComponent;
  let fixture: ComponentFixture<LivestreamPreviewComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ LivestreamPreviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LivestreamPreviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
