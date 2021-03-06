import React from 'react';
import { Button, Divider, Form, Grid, Segment } from 'semantic-ui-react';

export default class LoginBoxWithVerticalDivider extends React.Component {
    render() {
        return (
            <Segment placeholder>
                <Grid columns={2} relaxed="very" stackable>
                    <Grid.Column>
                        <Form>
                            <Form.Input
                                icon="user"
                                iconPosition="left"
                                label="Username"
                                placeholder="Username"
                                />
                            <Form.Input
                                icon="lock"
                                iconPosition="left"
                                label="Password"
                                type="password"
                                />
                            <Button content="Login" primary />
                        </Form>
                    </Grid.Column>

                    <Grid.Column>
                        <Button content="Sign up" icon="signup" size="big" />
                    </Grid.Column>
                </Grid>
                <Divider content="Or" vertical />
            </Segment>
        )}
};
