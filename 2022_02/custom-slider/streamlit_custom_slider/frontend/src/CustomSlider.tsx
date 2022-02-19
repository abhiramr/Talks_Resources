import React, { useEffect, useState }  from "react";

import {Streamlit,
  withStreamlitConnection,
  ComponentProps,

} from "streamlit-component-lib";

import { Slider } from "baseui/slider";
/**
 * We can use a Typescript interface to destructure the arguments from Python
 * and validate the types of the input
 */
 interface PythonArgs {
  label: string
  minValue?: number
  maxValue?: number
  initialValue: number[]
}

/**
 * Called by <CustomSlider />, renders the return value on screen.
 *
 * (props) => {code} is an arrow function, a shorter syntax for JS functions
 * equivalent to : function (props) { code; return <h1>Hello world</h1>};
 * or in Python, lambda props : return <h1>Hello world</h1>.
 *
 * When called, it will run then render on the browser the returned JSX block
 */
const CustomSlider = (props: ComponentProps) => {
  console.log(props.args);
  const {label, minValue, maxValue, initialValue}: PythonArgs = props.args;

  // This React component returns (and renders) this <h1> block
  const [value, setValue] = useState(initialValue)

  useEffect(() => Streamlit.setFrameHeight());
  return(
    <>
     <h3>{label}</h3>

    <Slider
        value={value}
        onChange={({ value }) => value && setValue(value)}
        onFinalChange={({ value }) => Streamlit.setComponentValue(value)}
        min={minValue}
        max={maxValue}
    />
  </>
  );
};

// Make the function publicly available. If you forget this, index.tsx won't find it.
// Link the component to Streamlit JS events.
export default withStreamlitConnection(CustomSlider);